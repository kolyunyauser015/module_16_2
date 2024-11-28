from fastapi import FastAPI, Path
from typing import Annotated
from enum import Enum


class Category(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"


app = FastAPI()


@app.get("/")
async def get_main_page() -> str:
    return "Главная страница"


@app.get("/user/admin")
async def get_admin_page() -> str:
    return "Вы вошли как администратор"


@app.get("/user/{user_id}")
async def get_user_namber(
        user_id: Annotated[
            int,
            Path(ge=1,
                 le=100,
                 description="Enter User ID",
                 example=1)
        ]
):
    return f"Вы вошли как пользователь № {user_id}"


@app.get("/user/{username}/age")
async def get_user_info(
        user_name: Annotated[
            str,
            Path(min_length=5,
                 max_length=20,
                 description="Enter username",
                 example="UrbanUser")],
        age: Annotated[
            int,
            Path(ge=12,
                 le=120,
                 description="Enter age",
                 example=24)
        ]
):
    return f"Информация о пользователе. Имя: {user_name}, Возраст: {age}"
