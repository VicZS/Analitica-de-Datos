from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import pymongo
from bson import ObjectId

from clienteA import cliente
from models.users import User,UserM,UserM1,UserA

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
    resultados = []
    cursor = collection.find({})  # Encuentra todos los documentos en la colección

    for documento in cursor:
        user = UserM(**documento)
        resultados.append({
            "id": str(documento["_id"]),
            **user.dict()
        })

    return resultados

# Funcion agregar
@router.post("/usuarios/agregar/", status_code=status.HTTP_201_CREATED, response_description="Usuario agregado correctamente")
async def agregar(user: UserM1):

    documento = user.dict()
    if not documento["id"] == None:
        if len(documento["id"]) < 24:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El id debe ser un valor de cadena hexadecimal de 24 caracteres")

    # Verificar si ya existe un objeto con el mismo nombre
    if collection.find_one({"_id": ObjectId(user.id)}):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe un Usuario con este id")
    
    documento["_id"]=ObjectId(user.id)
    documento.pop("id")
    documento["password"]=crypt.hash(user.password)

    resultado = collection.insert_one(documento)
    documento.pop("_id")
    documento["_id"]=str(resultado.inserted_id)
    documento = {"_id": documento.pop("_id"), **documento}

    return {"mensaje": "El Usuario se agrego exitosamente","Usuario": documento}


#Funcion actualizar

@router.put("/usuarios/actualizar/{id}", status_code=status.HTTP_200_OK, response_description="Usuario actualizado correctamente")
async def actualizar(id: str, user: User):
    actualizar_us = collection.update_one({"_id": ObjectId(id)}, {"$set": user.dict()})
    if actualizar_us.modified_count == 1:
        collection.update_one({"_id": ObjectId(id)}, {"$set": {"password": crypt.hash(user.password)}})
        return {"mensaje": "Usuario actualizado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado o No se realizaron cambios")

# Funcion Eliminar
@router.delete("/usuarios/eliminar/{id}", status_code=status.HTTP_200_OK, response_description="Usuario eliminado correctamente")
async def eliminar(id: str):
    eliminar_us = collection.delete_one({"_id": ObjectId(id)})
    if eliminar_us.deleted_count == 1:
        return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado")


'''

{
        "username":"a",
        "full_name":"a",
        "email":"a",
        "phone":1234,
        "password": "123",
        "dni":"a"
}

##agregar
{
        "id":"123456789012asdfgh",
        "username":"a",
        "full_name":"a",
        "email":"a",
        "phone":1234,
        "password": "123",
        "dni":"a",
        "disabled": "False"
}

'''


def search_user_db(username: str):
    users_db = list(collection.find({"username": username}))
    if any(user["username"] == username for user in users_db):
        return UserA(**users_db[0])


def search_user(username:str):
    users_db = collection.find({"username": username})
    if username in users_db:
        return UserA(**users_db[username])
    
async def auth_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")

    return search_user_db(username)

async def current_user(user_db: UserA = Depends(auth_user)):
    if user_db.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user_db


@router.post("/login/")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = search_user_db(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    if not crypt.verify(form.password, user_db.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.utcnow() + access_token_expiration
    access_token = {"sub": user_db.username, "exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}

@router.get("/users/me/")
async def me(user_db:UserA= Depends (current_user)):
    imagen = f"static/{user_db.username}.png"
    return FileResponse (imagen)