from pydantic import BaseModel


class FoodSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True