from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

router = APIRouter()

class Laptop(BaseModel):
    id: int
    CPU: str
    RAM: str
    Almacenamiento: str
    Marca: str
    SO: str

laptop_list=[
    Laptop(id=1, CPU = "Intel",RAM = "8GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=2, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=3, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=4, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=5, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=6, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=7, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=8, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=9, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=10, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=11, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=12, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=13, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=14, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=15, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=16, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=17, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=18, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=19, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=20, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=21, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=22, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=23, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=24, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=25, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" )
]

@router.get("/Apple/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de laptops correctamente")
async def laptopsclass():
    return (laptop_list)

@router.post("/Apple/", response_model=Laptop, status_code=status.HTTP_201_CREATED, response_description="La laptop se añadio correctamente")
async def laptopsclass(laptops:Laptop):
    found=False
    
    for index, saved_laptops in enumerate(laptop_list):
        if saved_laptops.id == laptops.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La laptop ya existe")
    else:
        laptop_list.append(laptops)
        return laptops
    
@router.put("/Apple/", response_model=Laptop, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la laptop se actualizo correctamente")
async def laptopsclass(laptops:Laptop):
    
    found=False

    for index, saved_pasajero in enumerate(laptop_list):
        if saved_pasajero.id == laptops.id:
            laptop_list[index] = laptops
            found=True
    
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontró la laptop con el ID proporcionado")
    else:
        return laptops, {"respuesta":"La informacion de la laptop se ha actualizado exitosamente!"}

@router.delete("/Apple/{id}", status_code=status.HTTP_202_ACCEPTED)
async def laptopsclass(id:int):
    
    found=False   
    
    for index, saved_laptop in enumerate(laptop_list):
        if saved_laptop.id ==id:
           del laptop_list[index] 
           found=True
           return "La laptop se ha eliminado correctamente"
    if not found:
        raise HTTPException(status_code= status.HTTP_404_NOT_FOUND,detail="No se encontro la laptop a eliminar")
        return {"error":"No se encontro la laptop a eliminar"}