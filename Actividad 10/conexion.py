import pymongo

MONGO_TIEMPO_FUERA=1000
MONGO_URL="mongodb://localhost:27017/"

try:
    cliente=pymongo.MongoClient(MONGO_URL,serverSelectionTimeoutMS=MONGO_TIEMPO_FUERA)
    cliente.server_info()
    print("Conexion a MongoDB exitosa")
    database = cliente["Prueba"]
    collection = database["laptops"]
    for documento in collection.find():
        print (documento)
    cliente.close()

except pymongo.errors.ServerSelectionTimeoutError as errorTiempo:
    print("Tiempo excedido"+errorTiempo)
except pymongo.errors.ConnectionFailure as errorConexion:
    print("Fallo al conectarse"+errorConexion)