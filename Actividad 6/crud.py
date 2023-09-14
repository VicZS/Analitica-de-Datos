from fastapi import FastAPI, HTTPException, status
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

@app.get("/pasajeros/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista correctamente")
async def pasajeros():
    return (pasajeros_list)

@app.post("/pasajeros/", response_model=Pasajeros, status_code=status.HTTP_201_CREATED, response_description="El pasajero se añadio correctamente")
async def pasajerosclass(pasajeros:Pasajeros):
    found=False
    
    for index, saved_pasajero in enumerate(pasajeros_list):
        if saved_pasajero.id == pasajeros.id:
            raise HTTPException(status_code= status.HTTP_401_UNAUTHORIZED,detail="el pasajero ya existe")
    else:
        pasajeros_list.append(pasajeros)
        return pasajeros
    
@app.put("/pasajeros/", response_model=Pasajeros, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion del pasajero se actualizo correctamente")
async def pasajerosclass(pasajeros:Pasajeros):
    
    found=False

    for index, saved_pasajero in enumerate(pasajeros_list):
        if saved_pasajero.id == pasajeros.id:
            pasajeros_list[index] = pasajeros
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró el pasajero con el ID proporcionado")
    else:
        return pasajeros, {"respuesta":"El pasajero se ha actualizado exitosamente!"}
    
@app.delete("/pasajeros/{id}", status_code=status.HTTP_202_ACCEPTED, response_description= "El pasajero se elimino correctamente")
async def pasajerosclass(id: int):
    global pasajeros_list

    updated_pasajeros_list = [pasajeros for pasajeros in pasajeros_list if pasajeros.id != id]

    if len(updated_pasajeros_list) == len(pasajeros_list):
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró el pasajero con el ID proporcionado")
    else:
        pasajeros_list = updated_pasajeros_list
        return {"message": "El pasajero se ha eliminado exitosamente"}