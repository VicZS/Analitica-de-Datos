from fastapi import FastAPI
import random

app = FastAPI()

cpu_brands = ["Intel", "AMD", "Apple_M1"]
ram_options = ["8GB", "16GB", "32GB"]
storage_options = ["256GB", "512GB", "1TB"]

def generar_laptops():
    laptops = []
    flist = []

    for _ in range(200):
        laptop = {
            "Modelo": f"laptop{_+1}",
            "CPU": random.choice(cpu_brands),
            "RAM": random.choice(ram_options),
            "Almacenamiento": random.choice(storage_options)
        }
        laptops.append(laptop)
    
    return laptops



@app.get("/")
async def imprimir():
    laptops = generar_laptops()
    output = ""
    for laptop in laptops:
        output += f"{laptop['Modelo']} = laptop('{laptop['CPU']}','{laptop['RAM']}','{laptop['Almacenamiento']}') "
    
    for laptop in laptops:
        output += f"{laptop['Modelo']}, "
    return output
