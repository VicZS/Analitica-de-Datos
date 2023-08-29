from fastapi import FastAPI
import random

app = FastAPI()

cpu_brands = ["Intel", "AMD", "Apple_M1"]
ram_options = ["8GB", "16GB", "32GB"]
storage_options = ["256GB", "512GB", "1TB"]
brands = ["HP", "Acer", "Apple", "Asus", "MSI"]
so = ["Windows", "MacOS", "Linux"]

def generar_laptops():
    laptops = []
    flist = []

    for _ in range(200):
        laptop = {
            "Modelo": f"id={_+1}",
            "CPU": random.choice(cpu_brands),
            "RAM": random.choice(ram_options),
            "Almacenamiento": random.choice(storage_options),
            "Marca": random.choice(brands),
            "SO": random.choice(so)
        }
        laptops.append(laptop)
    
    return laptops



@app.get("/")
async def imprimir():
    laptops = generar_laptops()
    output = ""
    for laptop in laptops:
        output += f"Laptop({laptop['Modelo']}, CPU = '{laptop['CPU']}',RAM = '{laptop['RAM']}',Almacenamiento = '{laptop['Almacenamiento']}', Marca = '{laptop['Marca']}', SO = '{laptop['SO']}' ) Y "
    
    for laptop in laptops:
        output += f"{laptop['Modelo']}, "
    return output
