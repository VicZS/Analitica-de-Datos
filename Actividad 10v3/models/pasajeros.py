#Importamos pydantic para obtener una entidad que pueda definir usuarios
from pydantic import BaseModel
from bson import ObjectId

class Pasajeros(BaseModel):
    _id: ObjectId | None
    name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: str
    Fare: str
    Cabin: str
    Embarked: str
    