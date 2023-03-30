from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sqlite3

app = Flask(__name__)

# mysql + pymysql : // usuario @ servidor / base de datos
cadenaConexion = "mysql+pymysql://root@localhost/tiendaorm"
app.config['SQLALCHEMY_DATABASE_URI']= cadenaConexion
app.config['UPLOAD_FOLDER']="./images"
# objeto que representa la base de datos
db = SQLAlchemy(app)

from controller.controllerInicio import *
# from controller.categoriaController import *
from controller.productoController import *

if __name__ == '__main__':
    app.run(debug=True,port=8080)