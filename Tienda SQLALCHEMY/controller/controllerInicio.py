from app import db, app
from flask import Flask
from model.categoria import *
from model.producto import *
from flask_sqlalchemy import SQLAlchemy

# crea las tablas de la base de datos sino existe 
with app.app_context():
    db.create_all()
    
@app.route('/')
def inicio():
    return "Se ha creado las tablas de las base de datos"