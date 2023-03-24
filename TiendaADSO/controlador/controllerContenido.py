from modelo.producto import *
from modelo.venta import *
from modelo.detalleVenta import *
from app import app,tienda
from flask import request,render_template, jsonify
import json

@app.route('/contenido')
def vistaContenido():
    return render_template('contenido.html')
