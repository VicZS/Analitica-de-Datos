from fastapi import FastAPI
import random
#"HP", "Acer", "Apple", "Asus", "MSI", "Lenovo", "Dell", "Razer", "Samsung",
app = FastAPI()

cpu_brands = ["Apple_M1", "Intel", "AMD"]
ram_options = ["8GB", "16GB", "32GB"]
storage_options = ["256GB", "512GB", "1TB"]
brands = ["Apple"]
so = ["MacOS", "Windows", "Linux"]

def generar_laptops():
    laptops = []
    flist = []

    for _ in range(25):
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
