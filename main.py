import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
import requests

print("hello")

app = FastAPI()

db = []

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
    return db

@app.get('/cities/{city_id}')
def get_city(city_id: int) -> City :
    return db[city_id - 1]

@app.post('/cities')
def create_city(city: City) -> City :
    db.append(city)
    #  return last item
    return db[-1]

@app.delete('/cities/{city_id')
def delete_city(id: int):
    db.pop(id)
    return db


if __name__ == "__main__":
    # browse to 127.0.0.1:8000/docs for swaagger
    uvicorn.run(app, host="0.0.0.0", port=8000)