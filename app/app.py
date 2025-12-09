from fastapi import FastAPI, HTTPException

app = FastAPI()

text_posts = {  1:{"title": "1st Post, yay!!", "content": "This is the 1st post content."},
                2:{"title": "2nd Post, yay!!", "content": "This is the 2nd post content."},
                3:{"title": "3rd Post, yay!!", "content": "This is the 3rd post content."},
                4:{"title": "4th Post, yay!!", "content": "This is the 4th post content."},
                5:{"title": "5th Post, yay!!", "content": "This is the 5th post content."},
                6:{"title": "6th Post, yay!!", "content": "This is the 6th post content."},
                7:{"title": "7th Post, yay!!", "content": "This is the 7th post content."},
                8:{"title": "8th Post, yay!!", "content": "This is the 8th post content."},
                9:{"title": "9th Post, yay!!", "content": "This is the 9th post content."},
                10:{"title": "10th Post, yay!!", "content": "This is the 10th post content."}
             }

@app.get("/hello-world")
def hello_world():
    return {"message": "Hello, World!"}

@app.get("post")
def get_all_posts():
    return text_posts

@app.get("/post/{id}")
def get_post(id: int):
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")
    return text_posts[id]