from app import app
from model.categoria import *
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

# =============================================================================
@app.route("/vistaAgregarCategoria")
def vistaCategoria():
    return render_template("frmAgregarCategoria.html")
                           

@app.route('/agregarCategoria', methods=['POST'])
def agregarCategoria():
    try:
        nombre = request.form['txtCategoria'].upper()
        categoria = Category(catNombre=nombre)
        db.session.add(categoria)
        db.session.commit()
        mensaje ="Categoria Agreggada Correctamente"
    except exc.SQLAlchemyError as ex:
        db.session.rollback()
        mensaje = str(ex)
    return redirect('/listaProductos')

# =============================================================================
@app.route('/obtenerCategoriaJson', methods=['GET'])
def obtenerCategoriasJson():
    listaCategorias = Category.query.all()
    listaJson = [] 
    for categoria in listaCategorias:
        categoria = {
            "idCategoria":categoria.idCategoria,
            "catNombre": categoria.catNombre
        }
        listaJson.append(categoria)
    return listaJson

@app.route('/agregarCategoriaJson', methods=['POST'])
def agregarCategoriaJson():
    try:
        datos = request.get_json()
        print(datos)
        categoria = Category(catNombre = datos['nombreCategoria'])
        db.session.add(categoria)
        db.session.commit()
        mensaje="Categoria Agregada"
    except exc.SQLAlchemyError as ex:
        db.session.rollback()
        mensaje = str(ex)
    return {"mensaje":mensaje}
# =============================================================================
