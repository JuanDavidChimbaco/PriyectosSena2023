from flask import Flask, request,render_template 
import pymongo
import os



app = Flask(__name__)
app.config['UPLOAD_FOLDER']= './static/img'

#se crea objeto conexion al servidor mongodb
miConexion = pymongo.MongoClient('mongodb://localhost:27017')

#acceso a la base de datos
baseDatos = miConexion["GESTIONPRODUCTOS"]
print(type(baseDatos))

#crear objeto que permite acceder a la coleccion productos

productos = baseDatos["PRODUCTOS"]
print(type(productos))

from controlador.controllerProducto import *

if __name__ == "__main__":
    app.run(port=3000,debug=True)