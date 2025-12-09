from fastapi import FastAPI, HTTPException, File, UploadFile, Depends, Form
from app.schemas import PostCreate
from app.db import Post, create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager
from sqlalchemy import select


'''
This function will be used to manage the lifespan of the FastAPI application.
This is done to ensure that the database tables are created when the application starts.
'''
@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)


@app.post("/upload")
async def upload_file(
        file: UploadFile = File(...),
        caption: str = Form(""),
        session: AsyncSession = Depends(get_async_session)
):
    
    post = Post(
        caption=caption,
        url="dummy url",
        file_type="photo",
        file_name="dummy name"
    )
    session.add(post)   # add the post object to the session
    await session.commit()  # commit the transaction, await is used because it would take time to complete. Writing await will not block the event loop. It will allow other tasks to run while waiting for the commit to complete.
    await session.refresh(post)  # refresh the post object to get the updated data from the database
    return post


@app.get("/feed")
async def get_feed(
    session: AsyncSession = Depends(get_async_session)
):
    result = await session.execute(select(Post).order_by(Post.created_at.desc()))
    posts = [row[0] for row in result.all()]    # convert list of tuples to list of Post objects

    posts_data = []
    
