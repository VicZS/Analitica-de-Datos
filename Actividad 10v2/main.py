from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse

app= FastAPI()
import pymongo

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION=1
SECRET="123456789"

app.mount("/static", StaticFiles(directory="static"), name="static")
oauth2=OAuth2PasswordBearer(tokenUrl="login")
crypt= CryptContext(schemes="bcrypt")

MONGO_TIEMPO_FUERA=1000
MONGO_URL="mongodb://localhost:27017/"

try:
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexion a MongoDB exitosa")

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse"+errorConexion)


database = cliente["Alumnos"]
collection = database["users_db"]

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

# Mostrar todos los objetos de mi bd
@app.get("/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultado2 = []
    for lista in collection.find():
        print (lista)
        resultado = str("username: "+lista["username"]+", full_name: "+lista["full_name"]+", email: "+lista["email"]+", phone: "+str(lista["phone"])+", disabled: "+lista["disabled"]+", dni: "+lista["dni"]+", password: "+lista["password"]) 
        resultado2.append(resultado)
    return (resultado2)

# Funcion agregar
@app.post("/agregar/", status_code=status.HTTP_201_CREATED, response_description="Usuario agregado correctamente")
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

@app.put("/actualizar/{nombre}", status_code=status.HTTP_200_OK, response_description="Usuario actualizado correctamente")
async def actualizar(nombre: str, user: UserU):
    actualizar_us = collection.update_one({"username": nombre}, {"$set": user.dict()})
    if actualizar_us.modified_count == 1:
        collection.update_one({"username": nombre}, {"$set": {"password": crypt.hash(user.password)}})
        return {"mensaje": "Usuario actualizado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrado o No se realizaron cambios")

# Funcion Eliminar
@app.delete("/eliminar/{nombre}", status_code=status.HTTP_200_OK, response_description="Usuario eliminado correctamente")
async def eliminar(nombre: str):
    eliminar_us = collection.delete_one({"username": nombre})
    if eliminar_us.deleted_count == 1:
        return {"mensaje": "Usuario eliminado correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuario no encontrada")

########################################################

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


@app.post("/login/")
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

@app.get("/users/me/")
async def me(user_db:UserA= Depends (current_user)):
    imagen = f"static/{user_db.username}.png"
    return FileResponse (imagen)