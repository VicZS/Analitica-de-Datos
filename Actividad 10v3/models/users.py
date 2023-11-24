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

class UserA(User):
    disabled:bool

class UserU(BaseModel):
    full_name:str
    email:str
    phone:int
    password:str