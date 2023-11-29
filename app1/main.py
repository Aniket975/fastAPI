from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel 
from random import randrange

app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":  "I am learning Fastapi", "content": "Learning it from a vedio", "id": 1, "rating": 10},
            {"title":  "Need to do more practice", "content": "Learning more things", "id": 2, "rating": 10}]

@app.get("/")
def root():
    return {"Message": "Welcome to my api"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}