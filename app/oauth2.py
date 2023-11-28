from jose import JWTError, jwt
from datetime import datetime, timedelta

#Secret_Key
#Algorithm
#expiration_time

SECRET_KEY = "09DKK600joa98llbfbk95klmkl5552yn26jnjn5bjb2bj5jnjn6jn2562k2k222opoo"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()

    expire = datetime.now() +  timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt
