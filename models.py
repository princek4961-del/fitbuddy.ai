
from pydantic import BaseModel

class UserInput(BaseModel):
    name:str
    age:int
    weight:int
    goal:str
    intensity:str
