#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
from routers import CRUD1 , CRUD2, CRUD3 #, router_DB_10

from fastapi.staticfiles import StaticFiles
#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(CRUD1.router)
app.include_router(CRUD2.router)
app.include_router(CRUD3.router)


#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Hola profe :D"
