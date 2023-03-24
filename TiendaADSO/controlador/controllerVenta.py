from modelo.producto import *
from modelo.venta import *
from modelo.detalleVenta import *
from app import app,tienda
from flask import request,render_template, jsonify
import json

@app.route('/vistaComprar')
def vistaComprar():
    return render_template('comprar.html')

@app.route('/obtenerListaProducto', methods=['GET'])
def obtenerListaProducto():
    listaProductos=[]
    for p in tienda.getListaProductos():
        producto = [p.getCodigo(),p.getNombre(),p.getPrecio()]
        listaProductos.append(producto)
    return jsonify({'datos':listaProductos})

@app.route('/obtenerListaCliente', methods=['GET'])
def obtenerListaClientes():
    listaClientes=[]
    for c in tienda.getListaClientes():
        cliente = [c.getIdentificacion(),c.getNombre(),c.getDireccion(),c.getCorreo()]
        listaClientes.append(cliente)
    return jsonify({'datos':listaClientes})