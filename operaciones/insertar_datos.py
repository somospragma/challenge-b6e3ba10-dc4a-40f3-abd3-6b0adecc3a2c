from pymongo import MongoClient

def insertar_usuario(client, usuario):
    db = client.get_database('fintech')
    usuarios = db.get_collection('usuarios')
    usuarios.insert_one(usuario)

def insertar_transaccion(client, transaccion):
    db = client.get_database('fintech')
    transacciones = db.get_collection('transacciones')
    transacciones.insert_one(transaccion)