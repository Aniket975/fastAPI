from typing import Optional,List
from fastapi import FastAPI, Response, status, HTTPException, Depends
import psycopg
from random import randrange
from time import sleep
from sqlalchemy.orm import Session
from . import models,schemas,utils
from .database import engine, get_db
from .routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

my_posts = [{"title": "title of post1",
             "content": "content of post 1", "id": 1},
            {"title": "title of post2",
             "content": "content of post2", "id": 2}]

while True:
    try:
        conn = psycopg.connect(
            "dbname=fastapi user=postgres password=Patna@123")
        cur = conn.cursor()
        print('Database connection was successfull!')
        break
    except Exception as error:
        print('Connecting to databse failed')
        print('Error: ', error)
        sleep(2)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
