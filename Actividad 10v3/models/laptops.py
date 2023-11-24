#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from bson import ObjectId

class Laptop(BaseModel):
    id: str | None
    CPU: str
    RAM: str
    Almacenamiento: str
    Marca: str
    SO: str