import os
from werkzeug.utils import secure_filename
from app import app
from model.categoria import *
from model.producto import *
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
 
@app.route('/listaProductos')
def listarProductos():
    try:
        listaProductos = Products.query.all()
        print(listarProductos)
        mensaje = "Listado de Productos"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return render_template('listarProductos.html', mensaje=mensaje, listarProductos=listaProductos)
      
      
@app.route('/api/listarProductos')
def apilistarProductos():
    try:
      listaProductos = Products.query.all()
      listaJson =[]
      for p in listaProductos:
          producto={
              "idProducto":p.idProducto
          }
          listaJson.append(p)
    except exc.Exe:
      print('An exception occurred')