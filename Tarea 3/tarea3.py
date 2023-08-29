from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Laptop(BaseModel):
    id: int
    CPU: str
    RAM: str
    Almacenamiento: str
    Marca: str
    SO: str

laptop_list=[
    Laptop(id=1, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=2, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=3, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=4, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=5, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=6, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=7, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=8, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=9, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=10, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=11, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=12, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=13, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=14, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=15, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=16, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=17, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=18, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=19, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=20, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=21, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=22, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=23, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=24, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=25, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=26, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=27, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "HP", SO = "Linux" ),
    Laptop(id=28, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=29, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=30, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=31, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=32, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=33, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=34, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=35, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=36, CPU = "Intel",RAM = "8GB",Almacenamiento = "512GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=37, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=38, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=39, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=40, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=41, CPU = "Intel",RAM = "8GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=42, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=43, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=44, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=45, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=46, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=47, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=48, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=49, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=50, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=51, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=52, CPU = "Intel",RAM = "8GB",Almacenamiento = "1TB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=53, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=54, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=55, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=56, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=57, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=58, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=59, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=60, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=61, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=62, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=63, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=64, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=65, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=66, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=67, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=68, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=69, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=70, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=71, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=72, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=73, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=74, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=75, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=76, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=77, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=78, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=79, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=80, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=81, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Linux" ),
    Laptop(id=82, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "HP", SO = "Linux" ),
    Laptop(id=83, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=84, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=85, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=86, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=87, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=88, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=89, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=90, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=91, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=92, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=93, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=94, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=95, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=96, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=97, CPU = "Intel",RAM = "8GB",Almacenamiento = "512GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=98, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=99, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=100, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=101, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=102, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=103, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=104, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=105, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Linux" ),
    Laptop(id=106, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=107, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=108, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=109, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=110, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=111, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=112, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=113, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=114, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=115, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=116, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=117, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=118, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=119, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=120, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=121, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=122, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=123, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=124, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=125, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=126, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=127, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=128, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=129, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=130, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=131, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=132, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=133, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=134, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=135, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=136, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=137, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=138, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=139, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=140, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=141, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=142, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=143, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=144, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "1TB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=145, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=146, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=147, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=148, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=149, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=150, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=151, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=152, CPU = "Intel",RAM = "8GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=153, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=154, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=155, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=156, CPU = "Intel",RAM = "16GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=157, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=158, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=159, CPU = "AMD",RAM = "32GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=160, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=161, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "256GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=162, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=163, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=164, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=165, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=166, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=167, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=168, CPU = "AMD",RAM = "32GB",Almacenamiento = "256GB", Marca = "Apple", SO = "MacOS" ),
    Laptop(id=169, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=170, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=171, CPU = "AMD",RAM = "8GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=172, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=173, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "HP", SO = "Windows" ),
    Laptop(id=174, CPU = "AMD",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=175, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=176, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=177, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=178, CPU = "Intel",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=179, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=180, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=181, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=182, CPU = "AMD",RAM = "8GB",Almacenamiento = "1TB", Marca = "HP", SO = "Windows" ),
    Laptop(id=183, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "MacOS" ),
    Laptop(id=184, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "512GB", Marca = "MSI", SO = "Linux" ),
    Laptop(id=185, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "HP", SO = "Linux" ),
    Laptop(id=186, CPU = "AMD",RAM = "32GB",Almacenamiento = "512GB", Marca = "Apple", SO = "Windows" ),
    Laptop(id=187, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "512GB", Marca = "Acer", SO = "Linux" ),
    Laptop(id=188, CPU = "Intel",RAM = "32GB",Almacenamiento = "1TB", Marca = "Apple", SO = "Linux" ),
    Laptop(id=189, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=190, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Acer", SO = "Windows" ),
    Laptop(id=191, CPU = "AMD",RAM = "16GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),
    Laptop(id=192, CPU = "Apple_M1",RAM = "8GB",Almacenamiento = "256GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=193, CPU = "Intel",RAM = "8GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=194, CPU = "Apple_M1",RAM = "32GB",Almacenamiento = "256GB", Marca = "MSI", SO = "Windows" ),
    Laptop(id=195, CPU = "AMD",RAM = "16GB",Almacenamiento = "512GB", Marca = "Asus", SO = "Linux" ),
    Laptop(id=196, CPU = "Apple_M1",RAM = "16GB",Almacenamiento = "1TB", Marca = "Asus", SO = "Windows" ),
    Laptop(id=197, CPU = "Intel",RAM = "16GB",Almacenamiento = "1TB", Marca = "HP", SO = "Linux" ),
    Laptop(id=198, CPU = "Intel",RAM = "16GB",Almacenamiento = "256GB", Marca = "Asus", SO = "MacOS" ),
    Laptop(id=199, CPU = "Intel",RAM = "32GB",Almacenamiento = "512GB", Marca = "HP", SO = "MacOS" ),
    Laptop(id=200, CPU = "AMD",RAM = "8GB",Almacenamiento = "256GB", Marca = "MSI", SO = "MacOS" ),]


@app.get("/")
async def imprimir():
    return laptop_list


@app.get("/laptopclass/{id}")
async def laptopclass(id:int):
    laptops = filter (lambda laptop: laptop.id == id, laptop_list)
    try:
        return list(laptops)[0]
    except:
        return{"error":"No se ha encontrado la laptop que buscas"}
    
@app.get("/laptopclass2/")
async def laptopclass(CPU:str, RAM:str):
    laptops=filter (lambda laptop: laptop.CPU == CPU, laptop_list)#Función de orden superior
    laptops1=filter (lambda laptop: laptop.RAM == RAM, laptops)#Función de orden superior
    try:
        return list(laptops1)[0] #Nota se borra el [0] para que se muestren todas las computadoras que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado el usuario"}
    
@app.get("/laptopclass3/")
async def laptopclass(CPU:str, RAM:str, Almacenamiento:str):
    laptops=filter (lambda laptop: laptop.CPU == CPU, laptop_list)#Función de orden superior
    laptops1=filter (lambda laptop: laptop.RAM == RAM, laptops)#Función de orden superior
    laptops2=filter (lambda laptop: laptop.Almacenamiento == Almacenamiento, laptops1)
    try:
        return list(laptops2)[0] #Nota se borra el [0] para que se muestren todas las computadoras que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado el usuario"}
    
@app.get("/laptopclass4/")
async def laptopclass(CPU:str, RAM:str, Almacenamiento:str, Marca:str):
    laptops=filter (lambda laptop: laptop.CPU == CPU, laptop_list)#Función de orden superior
    laptops1=filter (lambda laptop: laptop.RAM == RAM, laptops)#Función de orden superior
    laptops2=filter (lambda laptop: laptop.Almacenamiento == Almacenamiento, laptops1)
    laptops3=filter (lambda laptop: laptop.Marca == Marca, laptops2)
    try:
        return list(laptops3)[0] #Nota se borra el [0] para que se muestren todas las computadoras que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado el usuario"}
    
@app.get("/laptopclass5/")
async def laptopclass(CPU:str, RAM:str, Almacenamiento:str, Marca:str, SO:str):
    laptops=filter (lambda laptop: laptop.CPU == CPU, laptop_list)#Función de orden superior
    laptops1=filter (lambda laptop: laptop.RAM == RAM, laptops)#Función de orden superior
    laptops2=filter (lambda laptop: laptop.Almacenamiento == Almacenamiento, laptops1)
    laptops3=filter (lambda laptop: laptop.Marca == Marca, laptops2)
    laptops4=filter (lambda laptop: laptop.SO == SO, laptops3)
    try:
        return list(laptops4)[0] #Nota se borra el [0] para que se muestren todas las computadoras que coincidan con los filtros
    except:
        return{"error":"No se ha encontrado el usuario"}