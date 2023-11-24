from fastapi import FastAPI
import random

app = FastAPI()

cpu_brands = ["Intel", "AMD"]
ram_options = ["8GB", "16GB", "32GB"]
storage_options = ["256GB", "512GB", "1TB"]
marca = ['HP',"ASUS", "SAMSUNG", "ACER", "LENOVO"]
SO = ["Windows", "Linux"]

def generar_laptops():
    laptops = []
    flist = []

    for _ in range(10):
        laptop = {
            "Modelo": f"laptop{_+1}",
            "CPU": random.choice(cpu_brands),
            "RAM": random.choice(ram_options),
            "Almacenamiento": random.choice(storage_options),
            "Marca":random.choice(marca),
            "SO":random.choice(SO)
        }
        laptops.append(laptop)
    
    return laptops



@app.get("/")
async def imprimir():
    laptops = generar_laptops()
    output = ""
    for laptop in laptops:
        output += f"(CPU: {laptop['CPU']}', RAM: '{laptop['RAM']}', Almacenamiento: '{laptop['Almacenamiento']}', Marca: '{laptop['Marca']}',SO: '{laptop['SO']}'),"
    
    return output
