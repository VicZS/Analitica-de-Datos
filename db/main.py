#########################################Primera Parte################################################
# Instalación del framwork fastApi, código:
# -pip install fastapi-

#Instalación del Servidor Uvicorn, código:
#-pip install "uvicorn[standard]"-

# Instalación del framwork fastApi, código:
# -pip install fastapi[all]-

#Importamos el framework fastapi a nuestro entorno de trabajo
from fastapi import FastAPI 
#Importamos de la carpeta: "routers" el código o las clases: "routers_5" y "routers2_5"
from routers import router_DB_10 #, router_DB_10

from fastapi.staticfiles import StaticFiles
#Creamos un objeto a partir de la clase FastAPI
app= FastAPI()


app.include_router(router_DB_10.router)



#Creamos un router a partir de la clase router_DB_10
#app.include_router(router_DB_10.router)


#Utilizamos la (instancia) función get del framework FastAPI
@app.get("/")

#creamos la función asincrona "imprimir"
async def imprimir():
    return "Hola profe :D"
