from pydantic import BaseModel


class DrinkSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True