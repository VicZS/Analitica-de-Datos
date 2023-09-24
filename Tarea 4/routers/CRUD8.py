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
    Laptop(id=1, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=2, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=3, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=4, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=5, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=6, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=7, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=8, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=9, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=10, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=11, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=12, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=13, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=14, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=15, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=16, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=17, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=18, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=19, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=20, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Windows" ),
    Laptop(id=21, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=22, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=23, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=24, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Samsung", SO = "Linux" ),
    Laptop(id=25, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Samsung", SO = "Linux" )
]

@router.get("/Samsung/", status_code=status.HTTP_202_ACCEPTED, response_description="Se devolvio la lista de laptops correctamente")
async def laptopsclass():
    return (laptop_list)

@router.post("/Samsung/", response_model=Laptop, status_code=status.HTTP_201_CREATED, response_description="La laptop se añadio correctamente")
async def laptopsclass(laptops:Laptop):
    found=False
    
    for index, saved_laptops in enumerate(laptop_list):
        if saved_laptops.id == laptops.id:
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,detail="La laptop ya existe")
    else:
        laptop_list.append(laptops)
        return laptops
    
@router.put("/Samsung/", response_model=Laptop, status_code=status.HTTP_202_ACCEPTED, response_description="La informacion de la laptop se actualizo correctamente")
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

@router.delete("/Samsung/{id}", status_code=status.HTTP_202_ACCEPTED)
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