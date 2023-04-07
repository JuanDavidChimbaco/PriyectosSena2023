from app import app , db
from flask import redirect, Flask
from flask_sqlalchemy import SQLAlchemy

from model.categoria import *
from model.producto import *

# crea las tablas de la base de datos sino existe 
with app.app_context():
    db.create_all()
    
@app.route('/')
def inicio():
    return redirect('/listaProductos')