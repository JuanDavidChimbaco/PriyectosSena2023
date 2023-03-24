from modelo.cliente import *
from app import app, tienda
from flask import request, render_template, jsonify


@app.route("/vistaAgregarCliente")
def vistaAgregarCliente():
    return render_template("frmAgregarCliente.html")

@app.route("/agregarCliente",methods=["POST"])
def agregarCliente():
    mensaje,estado=None,False
    try:
        identificacion = request.form["txtIdentificacion"]
        nombre = request.form["txtNombre"]
        direccion = request.form["txtDireccion"]
        correo = request.form["txtCorreo"]
        cliente = Cliente(identificacion,nombre,direccion,correo)
        tienda.agregarCliente(cliente)
        estado=True
        mensaje="Cliente Agregado Correctamente"
    except Exception as error:
        mensaje=error
    return render_template("frmAgregarCliente.html",mensaje=mensaje,estado=estado)
        
@app.route("/listaClientes")
def listaClientes():
    listaClientes  = tienda.getListaClientes()
    return render_template("listarCliente.html", listaClientes = listaClientes)

"""@app.route("/obtenerListaClientes",methods=["GET"])
def obtenerListaClientes():
    listaClientes=[]
    for c in tienda.getListaClientes():
        cliente =[c.getIdentificacion(),c.getNombre(),c.getDireccion(),c.getCorreo()]
        listaClientes.append(cliente)
    return jsonify({"datos": listaClientes})"""