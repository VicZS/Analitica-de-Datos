#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from bson import ObjectId

class Laptop(BaseModel):
    _id: ObjectId | None
    CPU: str
    RAM: str
    Almacenamiento: str
    Marca: str
    SO: str

class Laptop2(BaseModel):
    id: str | None
    CPU: str
    RAM: str
    Almacenamiento: str
    Marca: str
    SO: str    