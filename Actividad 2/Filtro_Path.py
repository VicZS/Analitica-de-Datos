from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    id: int
    Name: str
    LastName: str
    Age: int

users_list= [User(id=0,Name="Alfredo",LastName="Garcia",Age=30),
            User(id=1,Name="Juan",LastName="Perez",Age=45),
            User(id=2,Name="Maria",LastName="Lopez",Age=22)]

@app.get("/usersclass/{id}")
async def userclass(id:int):
    users = filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}