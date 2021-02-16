from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()


class User(BaseModel):
    user: str
    id: int
    email: str


@app.post("/user/")
def set_user(user: User):
    return {"key": user}


@app.get("/user/{user_id}", response_model=User)
def main(user_id: int):
    user = {
        "user": "Mike",
        "id": 2,
        "email": "cfsad@mail.ru"
    }
    return user
