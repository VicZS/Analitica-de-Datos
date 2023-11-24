#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from bson import ObjectId

class User(BaseModel):
    username:str
    full_name:str
    email:str
    phone:int
    dni:str
    password:str

class UserM(User):
    _id: ObjectId | None
    disabled: str

class UserM1(User):
    id: str | None
    disabled: str

class UserA(User):
    disabled:bool