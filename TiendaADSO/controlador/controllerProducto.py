from app import app,tienda
from modelo.producto import *
from flask import request,render_template,jsonify

@app.route("/vistaAgregarProducto")
def vistaAgregarProducto():
    return render_template("frmAgregarProducto.html")

@app.route("/agregarProducto",methods=["POST"])
def agregarProducto():
    mensaje=None
    estado=False
    try:
        codigo = int(request.form["txtCodigo"])
        nombre = request.form["txtNombre"]
        precio = int(request.form["txtPrecio"])
        producto = Producto(codigo,nombre,precio)
        tienda.agregarProducto(producto)
        estado=True
        mensaje="Producto Agregado Correctamente"
    except Exception as error:
        mensaje=error
    return render_template("frmAgregarProducto.html",mensaje=mensaje,estado=estado)
        
@app.route("/listarProductos")
def listarProductos():
    listaProductos  = tienda.getListaProductos()
    return render_template("listarProductos.html", listaProductos = listaProductos)

"""@app.route("/obtenerListaProductos",methods=["GET"])
def obtenerListaProductos():
    listaProductos=[]
    for p in tienda.getListaProductos():
        producto =[p.getCodigo(),p.getNombre(),p.getPrecio()]
        listaProductos.append(producto)
    return jsonify({"datos": listaProductos})"""