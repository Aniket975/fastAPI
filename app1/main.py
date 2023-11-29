from typing import Optional
from fastapi import FastAPI, status, HTTPException, Response
from pydantic import BaseModel 
from random import randrange

app = FastAPI(title="Aniket API")

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

my_posts = [{"title":  "I am learning Fastapi", "content": "Learning it from a vedio", "id": 1, "rating": 10},
            {"title":  "Need to do more practice", "content": "Learning more things", "id": 2, "rating": 10}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

def find_index_post(id):
    i = 0
    for p in my_posts:
        if p['id'] == id:
            return i
        i += 1


@app.get("/")
def root():
    return {"Message": "Welcome to my api"}

@app.get("/posts")
def get_post():
    return {"data": my_posts}

@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Data with id {id} not found')
    return {"data": post}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.put("/posts/{id}")
def update_post(id: int, post: Post):
    index = find_index_post(id)
    if index == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Kuch nahi mila bhai")
    post_dict = post.dict()
    post_dict['id'] = id
    my_posts[index] = post_dict
    return {'data': post_dict}


@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def create_posts(id: int):
    index = find_index_post(id)
    if not index:
        raise HTTPException(status.HTTP_404_NOT_FOUND,detail=f'Data with id {id} not found')
    my_posts.pop(index)
    return None


