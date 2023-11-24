from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from jose import jwt, JWTError
import pymongo

from models.laptops import Laptop,Laptop2
from clienteA import cliente

router = APIRouter()

database = cliente["Computadoras"]
collection = database["Laptops"]

# Mostrar todos los objetos de mi bd
@router.get("/laptops/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultados = []
    cursor = collection.find({})  # Encuentra todos los documentos en la colección

    for documento in cursor:
        laptop = Laptop(**documento)
        resultados.append({
            "id": str(documento["_id"]),
            **laptop.dict()
        })

    return resultados

@router.post("/laptops/agregar/", response_description="Laptop agregada correctamente")
async def agregar_laptop(laptop: Laptop2):

    documento = laptop.dict()

    if not documento["id"] == None:
        if len(documento["id"]) < 24:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El id debe ser un valor de cadena hexadecimal de 24 caracteres")

    if collection.find_one({"_id": ObjectId(laptop.id)}):
        raise HTTPException(status_code=400, detail="Ya existe un objeto con el mismo ID")
    
    documento["_id"]=ObjectId(laptop.id)
    documento.pop("id")

    resultado = collection.insert_one(documento)
    documento.pop("_id")
    documento["_id"]=str(resultado.inserted_id)
    documento = {"_id": documento.pop("_id"), **documento}

    return {"mensaje": "La Laptop se agrego exitosamente","Laptop": documento}

#Funcion actualizar

@router.put("/laptops/actualizar/{laptop_id}", status_code=status.HTTP_200_OK, response_description="Laptop actualizada correctamente")
async def actualizar_laptop(laptop_id: str, nuevo_laptop: Laptop):
    result = collection.update_one({"_id": ObjectId(laptop_id)}, {"$set": nuevo_laptop.dict()})
    if result.modified_count == 1:
        return {"message": "Laptop modificado exitosamente"}
    else:
        raise HTTPException(status_code=404, detail="Laptop no encontrada o no hay modificaciones que hacer")

@router.delete("/laptops/eliminar/{id}", status_code=status.HTTP_200_OK, response_description="Laptop eliminada correctamente")
async def eliminar(id: str):
    eliminar_us = collection.delete_one({"_id": ObjectId(id)})
    if eliminar_us.deleted_count == 1:
        return {"mensaje": "Laptop eliminada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop no encontrada")


'''
{
    "id": null,
    "CPU": "Intel",
    "RAM": "8GB",
    "Almacenamiento": "256GB",
    "Marca": "HP",
    "SO": "Windows"
}
'''