from fastapi import FastAPI 
from pydantic import BaseModel
app= FastAPI()

class Pasajeros(BaseModel):
    id: int
    Name: str
    Pclass: int
    Survived: int
    Sex: str
    Age: int
    SibSp: int
    Parch: int
    Ticket: str
    Fare: str
    Cabin: str
    Embarked: str

pasajeros_list=[]

@app.get("/pasajeros/")
async def pasajeros():
    return (pasajeros_list)

@app.post("/pasajeros/")
async def pasajerosclass(pasajeros:Pasajeros):
    found=False
    
    for index, saved_pasajero in enumerate(pasajeros_list):
        if saved_pasajero.id == pasajeros.id:
            return {"error":"el pasajero ya existe"}
    else:
        pasajeros_list.append(pasajeros)
        return pasajeros
    
@app.put("/pasajeros/")
async def pasajerosclass(pasajeros:Pasajeros):
    
    found=False

    for index, saved_pasajero in enumerate(pasajeros_list):
        if saved_pasajero.id == pasajeros.id:
            pasajeros_list[index] = pasajeros
            found=True
    
    if not found:
        return{"error":"No se ha actualizado el pasajero"}
    else:
        return pasajeros, {"respuesta":"El pasajero se ha actualizado exitosamente!"}
    
@app.delete("/pasajeros/{id}")
async def pasajerosclass(id: int):
    global pasajeros_list

    updated_pasajeros_list = [pasajeros for pasajeros in pasajeros_list if pasajeros.id != id]

    if len(updated_pasajeros_list) == len(pasajeros_list):
        return {"error": "No se encontró el pasajero con el ID proporcionado"}
    else:
        pasajeros_list = updated_pasajeros_list
        return {"message": "El pasajero se ha eliminado exitosamente"}