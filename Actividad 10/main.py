from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
app= FastAPI()

import pymongo

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


database = cliente["Prueba"]
collection = database["laptops"]

class Laptop(BaseModel):
    Nombre: str
    Marca: str


# Mostrar todos los objetos de mi bd
@app.get("/mostrar/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def mostrar():
    resultado2 = []
    for documento in collection.find():
        print (documento)
        resultado = str("Nombre: "+documento["Nombre"]+", Marca: "+documento["Marca"]) 
        resultado2.append(resultado)
    return (resultado2)



# Funcion agregar
@app.post("/agregar/", status_code=status.HTTP_201_CREATED, response_description="Laptop agregado correctamente")
async def agregar(laptop: Laptop):

    # Verificar si ya existe un objeto con el mismo nombre
    validar_laptop = collection.find_one({"Nombre": laptop.Nombre})
    if validar_laptop:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Ya existe una laptop con este nombre")

    nueva_laptop = {
        "Nombre": laptop.Nombre,
        "Marca": laptop.Marca
    }
    #Agregar objeto a la coleccion
    resultado = collection.insert_one(nueva_laptop)
    return {"mensaje": "Laptop creada exitosamente", "id_creado": str(resultado.inserted_id)}


#Funcion actualizar

@app.put("/actualizar/{nombre}", status_code=status.HTTP_200_OK, response_description="Laptop actualizada correctamente")
async def actualizar(nombre: str, laptop: Laptop):
    actualizar_obj = collection.update_one({"Nombre": nombre}, {"$set": laptop.dict()})
    if actualizar_obj.modified_count == 1:
        return {"mensaje": "Laptop actualizada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop no encontrada")


# Funcion Eliminar
@app.delete("/eliminar/{nombre}", status_code=status.HTTP_200_OK, response_description="Laptop eliminada correctamente")
async def eliminar(nombre: str):
    eliminar_obj = collection.delete_one({"Nombre": nombre})
    if eliminar_obj.deleted_count == 1:
        return {"mensaje": "Laptop eliminada correctamente"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop no encontrada")
