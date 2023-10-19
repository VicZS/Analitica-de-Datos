from fastapi import FastAPI, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from fastapi.staticfiles import StaticFiles

from fastapi.responses import FileResponse

#14 alumnos
ALGORITHM = "HS256"

ACCESS_TOKEN_DURATION=2

SECRET="123456789"

app= FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

oauth2=OAuth2PasswordBearer(tokenUrl="login")

crypt= CryptContext(schemes="bcrypt")

class User(BaseModel):
    username:str
    full_name:str
    email:str
    phone:int
    disabled:bool
    dni:str

class UserDB(User):
    password:str


users_db ={
    "FREDDY":{
        "username":"FREDDY",
        "full_name": "Freddy García",
        "email": "alfredo.garcias@alumno.buap.mx",
        "phone":2224237171,
        "disabled": False,
        "password": "$2a$12$Px4/G9Onxs4m6QxjAwsbtOmqf4BFxkLUvn3F5PFPbWmhWLYEyGObG",#"1234"
        "dni": "FREDDY"
    },
    "YOSS":{
        "username":"YOSS",
        "full_name": "Yosselin Pablo",
        "email": "yoss@alumno.buap.mx",
        "phone":2288358188,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "YOSS"
    },
    "ABRAHAM":{
        "username":"ABRAHAM",
        "full_name": "Abraham Coagtle Temis",
        "email": "abraham.coagtle@alumno.buap.mx",
        "phone":2731327748,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "ABRAHAM"
    },
    "ESTEFANIA":{
        "username":"ESTEFANIA",
        "full_name": "Estefania Rodriguez Martinez",
        "email": "estefania.rodriguezma@alumno.buap.mx",
        "phone":2288358188,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "ESTEFANIA"
    },
    "JUAN":{
        "username":"JUAN",
        "full_name": "Juan Pablo Mendoza Armas",
        "email": "juan.mendozaar@alumno.buap.mx",
        "phone":2281776285,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "JUAN"
    },
    "KEVIN":{
        "username":"KEVIN",
        "full_name": "Kevin Armas Hernandez",
        "email": "kevin.armas@alumno.buap.mx",
        "phone":6141998990,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "KEVIN"
    },
    "LUIS":{
        "username":"LUIS",
        "full_name": "Luis Castro Nava",
        "email": "luis.castron@alumno.buap.mx",
        "phone":8110502639,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "LUIS"
    },
    "PILAR":{
        "username":"PILAR",
        "full_name": "Pilar Hernandez Zambrano",
        "email": "pilar.hernandezz@alumno.buap.mx",
        "phone":201929897,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "PILAR"
    },
    "VICENTE":{
        "username":"VICENTE",
        "full_name": "Vicente Zavaleta Sanchez",
        "email": "vicente.zavaletas@alumno.buap.mx",
        "phone":2212671849,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "VICENTE"
    },
    "VICTOR":{
        "username":"VICTOR",
        "full_name": "Victor Manuel Rosales Zayas",
        "email": "victor.rosalesz@alumno.buap.mx",
        "phone":2224415653,
        "disabled": False,
        "password": "$2a$12$y6WJw8AD5QfZBoKAjq7FdOEPe2dWArGsjz5XZWy28PGpxRZHHYXm.",#5678
        "dni": "VICTOR"
    }
}

################################################################

def search_user_db(username:str):
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username:str):
    if username in users_db:
        return User(**users_db[username])
    
async def auth_user(token:str=Depends(oauth2)):
    try:
        username= jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")
    
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autenticación inválidas")

    return search_user(username)

async def current_user(user:User = Depends(auth_user)):
    if user.disabled:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Usuario inactivo")
    return user

@app.post("/login/")
async def login(form:OAuth2PasswordRequestForm= Depends()):
    user_db= users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    user= search_user_db(form.username)     
    if not crypt.verify(form.password,user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    access_token_expiration=timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire=datetime.utcnow()+access_token_expiration
    
    access_token={"sub": user.username,"exp": expire}
    return {"access_token": jwt.encode(access_token, SECRET,algorithm=ALGORITHM), "token_type":"bearer"}

@app.get("/users/me/")
async def me(user:User= Depends (current_user)):
    imagen = f"static/{user.dni}.png"
    return FileResponse (imagen)
