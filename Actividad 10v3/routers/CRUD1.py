from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import pymongo

from clienteA import cliente
from models.users import User
from models.users import UserA
from models.users import UserU

router = APIRouter()

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION=1
SECRET="123456789"

router.mount("/static", StaticFiles(directory="static"), name="static")
oauth2=OAuth2PasswordBearer(tokenUrl="login")
crypt= CryptContext(schemes="bcrypt")


database = cliente["Alumnos"]
collection = database["users_db"]



# Mostrar todos los objetos de mi bd
@router.get("/usuarios/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultado2 = []
    for lista in collection.find():
        print (lista)
        resultado = str("id: "+str(lista["_id"])+", username: "+lista["username"]+", full_name: "+lista["full_name"]+", email: "+lista["email"]+", phone: "+str(lista["phone"])+", disabled: "+lista["disabled"]+", dni: "+lista["dni"]+", password: "+lista["password"]) 
        resultado2.append(resultado)
    return (resultado2)

# Funcion agregar
@router.post("/usuarios/agregar/", status_code=status.HTTP_201_CREATED, response_description="Usuario agregado correctamente")
async def agregar(user: User):

    # Verificar si ya existe un objeto con el mismo nombre
    validar_laptop = collection.find_one({"username": user.username})
    if validar_laptop:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un Usuario con este username")

    nuevo_user = {
        "username":user.username,
        "full_name":user.full_name,
        "email":user.email,
        "phone":user.phone,
        "disabled":"False",
        "password": crypt.hash(user.password),
        "dni":user.dni
    }

    
    #Agregar objeto a la coleccion
    resultado = collection.insert_one(nuevo_user)
    return {"mensaje": "El usuario se agrego exitosamente", "id_creado": str(resultado.inserted_id)}


#Funcion actualizar

@router.put("/usuarios/actualizar/{nombre}", status_code=status.HTTP_200_OK, response_description="Usuario actualizado correctamente")
async def actualizar(nombre: str, user: UserU):
    actualizar_us = collection.update_one({"username": nombre}, {"$set": user.dict()})
    if actualizar_us.modified_count == 1:
        collection.update_one({"username": nombre}, {"$set": {"password": crypt.hash(user.password)}})
        return {"mensaje": "Usuario actualizado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado o No se realizaron cambios")

# Funcion Eliminar
@router.delete("/usuarios/eliminar/{nombre}", status_code=status.HTTP_200_OK, response_description="Usuario eliminado correctamente")
async def eliminar(nombre: str):
    eliminar_us = collection.delete_one({"username": nombre})
    if eliminar_us.deleted_count == 1:
        return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrada")
