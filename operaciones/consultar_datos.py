from pymongo import MongoClient

def consultar_usuario(client, usuario_id):
    db = client.get_database('fintech')
    usuarios = db.get_collection('usuarios')
    return usuarios.find_one({'usuario_id': usuario_id})

def consultar_transaccion(client, transaccion_id):
    db = client.get_database('fintech')
    transacciones = db.get_collection('transacciones')
    return transacciones.find_one({'transaccion_id': transaccion_id})