from fastapi import FastAPI
app= FastAPI()
@app.get("/")

async def imprimir():
    return "Hola estudiantes"