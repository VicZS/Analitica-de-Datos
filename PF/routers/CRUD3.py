from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from jose import jwt, JWTError


from models.pasajeros import Pasajeros, Pasajeros2
from clienteA import cliente

router = APIRouter()

database = cliente["Titanic"]
collection = database["pasajeros"]

# Mostrar todos los objetos de mi bd
@router.get("/pasajeros/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultados = []
    cursor = collection.find({})  # Encuentra todos los documentos en la colección

    for documento in cursor:
        pasajero = Pasajeros(**documento)
        resultados.append({
            "id": str(documento["_id"]),
            **pasajero.dict()
        })

    return resultados

# Agregar un nuevo pasajero
@router.post("/pasajeros/agregar/", status_code=status.HTTP_201_CREATED, response_description="Pasajero agregado exitosamente")
async def agregar_pasajero(pasajero: Pasajeros2):

    documento = pasajero.dict()

    if not documento["id"] == None:
        if len(documento["id"]) < 24:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El id debe ser un valor de cadena hexadecimal de 24 caracteres")


    if collection.find_one({"_id": ObjectId(pasajero.id)}):
        raise HTTPException(status_code=400, detail="Ya existe un objeto con el mismo ID")    

    documento["_id"]=ObjectId(pasajero.id)
    documento.pop("id")

    resultado = collection.insert_one(documento)
    documento.pop("_id")
    documento["_id"]=str(resultado.inserted_id)
    documento = {"_id": documento.pop("_id"), **documento}

    return {"mensaje": "El Pasajero se agrego exitosamente","Pasajero": documento}

# Actualizar un pasajero existente
@router.put("/pasajeros/actualizar/{pasajero_id}", response_description="Pasajero modificado exitosamente")
async def actualizar_pasajero(pasajero_id: str, nuevo_pasajero: Pasajeros):
    result = collection.update_one({"_id": ObjectId(pasajero_id)}, {"$set": nuevo_pasajero.dict()})
    if result.modified_count == 1:
        return {"message": "Pasajero modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Pasajero no encontrado o no hay modificaciones que hacer")

# Eliminar un pasajero
@router.delete("/pasajeros/eliminar/{pasajero_id}", response_description="Pasajero eliminado exitosamente")
async def eliminar_pasajero(pasajero_id: str):
    result = collection.delete_one({"_id": ObjectId(pasajero_id)})
    if result.deleted_count == 1:
        return {"message": "Pasajero eliminado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Pasajero no encontrado")


'''
Formato del objeto

{
    "id": "656019869c1edd96c01b9495",
    "name": "Ejemplo",
    "Pclass": 1,
    "Survived": 1,
    "Sex": "Femenino",
    "Age": 25,
    "SibSp": 1,
    "Parch": 0,
    "Ticket": "12345",
    "Fare": "50.00",
    "Cabin": "C23",
    "Embarked": "S"
}
'''