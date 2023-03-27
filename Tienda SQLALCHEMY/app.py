from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# mysql + pymysql : // usuario @ servidor / base de datos
cadenaConexion = "mysql+pymysql://root@localhost/tiedaorm"
app.config['SQLALCHEMY_DATABASE_URI']= cadenaConexion

db = SQLAlchemy(app)

from modelo.categoria import *

if __name__ == '__main__':
    app.run(debug=True,port=8080)