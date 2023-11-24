from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from bson import ObjectId
from jose import jwt, JWTError
import pymongo

from models.laptops import Laptop
from clienteA import cliente

router = APIRouter()


database = cliente["Computadoras"]
collection = database["Laptops"]

# Mostrar todos los objetos de mi bd
@router.get("/laptops/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultado2 = []
    for lista in collection.find():
        print (lista)
        resultado = str("id: "+str(lista["_id"])+", CPU: "+lista["CPU"]+", RAM: "+lista["RAM"]+", Almacenamiento: "+lista["Almacenamiento"]+", Marca: "+lista["Marca"]+", SO: "+lista["SO"]) 
        resultado2.append(resultado)
    return (resultado2)

@router.post("/laptops/agregar/", response_description="Laptop agregada correctamente")
async def agregar_laptop(laptop: Laptop):
    # Verificar si ya existe un objeto con el mismo ID
    if collection.find_one({"_id": ObjectId(laptop.id)}):
        raise HTTPException(status_code=400, detail="Ya existe un objeto con el mismo ID")
    
    nueva_laptop = {
        "_id": ObjectId(laptop.id),
        "CPU": laptop.CPU,
        "RAM": laptop.RAM,
        "Almacenamiento": laptop.Almacenamiento,
        "Marca": laptop.Marca,
        "SO": laptop.SO
    }

    
    #Agregar objeto a la coleccion
    resultado = collection.insert_one(nueva_laptop)
    return {"mensaje": "La Laptop se agrego exitosamente", "id_creado": str(resultado.inserted_id)}

#Funcion actualizar

@router.put("/laptops/actualizar/{id}", status_code=status.HTTP_200_OK, response_description="Laptop actualizada correctamente")
async def actualizar(id: str, laptop: Laptop):
    if collection.find_one({"_id": ObjectId(laptop.id)}):

        actualizar_laptop = {
        "_id": ObjectId(laptop.id),
        "CPU": laptop.CPU,
        "RAM": laptop.RAM,
        "Almacenamiento": laptop.Almacenamiento,
        "Marca": laptop.Marca,
        "SO": laptop.SO
    }
        collection.update_one({"_id":ObjectId(id)}, {"$set": actualizar_laptop})
        return {"mensaje": "Laptop actualizada correctamente"}
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop no encontrada")

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