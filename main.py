import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import requests
from schemas.food_schema import FoodSchema
from fastapi_sqlalchemy import db
from fastapi_sqlalchemy import DBSessionMiddleware
from models import Food
import os
from fastapi.exceptions import HTTPException

print("hello")

app = FastAPI()
# TODO this should read from .env in docker, and from a local env.py, but I can't get
# dotenv installed and working (windows)
# app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.add_middleware(DBSessionMiddleware, db_url="postgresql+psycopg2://postgres:postgres@localhost:5432")

memory_db = []

class City(BaseModel):
    # the city name
    name: str
    # the city timezone food
    timezone: str
    population: int

@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/cities')
def get_cities():
    return memory_db

@app.get('/cities/{city_id}')
def get_city(city_id: int) -> City :
    return memory_db[city_id - 1]

@app.post('/cities')
def create_city(city: City) -> City :
    memory_db.append(city)
    #  return last item
    return memory_db[-1]

@app.delete('/cities/{city_id')
def delete_city(id: int):
    memory_db.pop(id)
    return memory_db


@app.post('/food', response_model=FoodSchema, name="Add Food to db")
def add_food(food: FoodSchema):

    existing_food = db.session.query(Food).get(food.id)

    if (existing_food):
        raise HTTPException(
                status_code=400,
                detail="This food already exists!",
        )


    db_food = Food(id = food.id, name = food.name)
    # TODO check if food by ID already exists. DB will throw an exception on its own though


    db.session.add(db_food)
    db.session.commit()
    return db_food

@app.get('/food', name="Get all Foods")
def get_foods():
    return db.session.query(Food).all()


if __name__ == "__main__":
    # browse to 127.0.0.1:8000/docs for swaagger
    # note: run `alembic upgrade head` if you created a new migration!
    # or run uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=800)