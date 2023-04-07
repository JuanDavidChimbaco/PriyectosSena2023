import os
from werkzeug.utils import secure_filename
from app import app
from model.categoria import *
from model.producto import *
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

# =============================================================================
@app.route('/listaProductos')
def listarProductos():
    try:
        listaProductos = Products.query.all()
        print(listarProductos)
        mensaje = "Listado de Productos"
    except exc.SQLAlchemyError as ex:
        mensaje = str(ex)
    return render_template('listarProductos.html', 
                           mensaje=mensaje, 
                           listarProductos=listaProductos)


@app.route("/vistaAgregarProducto")
def vistaProducto():
    producto = None
    #obtener las categorias que se muestran en el select del formulario

    listaCategorias = Category.query.all()
    return render_template("frmAgregarProducto.html",
                           producto = producto, 
                           listaCategorias = listaCategorias)

@app.route('/agregarProducto', methods=['POST'])
def agregarProducto():
    try:
        codigo = int(request.form["txtCodigo"])
        nombre = request.form["txtNombre"]
        precio = int(request.form["txtPrecio"])
        categoria = request.form["cbCategoria"]
        # Crear objeto producto
        producto = Products(proCodigo=codigo,
                            proNombre=nombre,
                            proPrecio=precio,
                            proCategoria=categoria)

        db.session.add(producto)
        db.session.commit()
        # ****************************
        archivo = request.files["fileFoto"]
        nombreArchivo = secure_filename(archivo.filename)
        listaNombreArchivo = nombreArchivo.rsplit(".", 1)
        extension = listaNombreArchivo[1].lower()
        # El nombre del archivo se incluirá el id del producto que
        # se acaba de registrar y la extension
        nuevoNombre = str(producto.idProducto) + "." + extension
        # Guardamos al archivo en el directorio "Archivos jpg"
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nuevoNombre))
        mensaje = "Producto Agregado Correctamente"
        return redirect("/listaProductos")

    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje = str(error)
        return render_template("frmAgregarProducto.html",
                           mensaje=mensaje,
                           producto=producto)


@app.route("/consultarProducto/<int:idProducto>", methods=["GET"])
def consultarProducto(idProducto):
    try:
        producto = Products.query.get(idProducto)
        listaCategoria = Category.query.all()

    except exc.SQLAlchemyError as error:
        mensaje = str(error)

    return render_template("frmActualizarProducto.html",
                           producto=producto,
                           listaCategoria=listaCategoria)

@app.route("/actualizarProducto", methods=["POST"])
def actualizarProducto():
    try:
        idProducto = request.form["idProducto"]
        producto = Products.query.get(idProducto)
        
        producto.proCodigo = request.form["txtCodigo"]
        producto.proNombre = request.form["txtNombre"]
        producto.proPrecio = request.form["txtPrecio"]
        producto.proCategoria = request.form["cbCategoria"]
        db.session.commit()
        
        archivo = request.files['fileFoto']
        if(archivo.filename != ""):
            nombreArchivo = secure_filename(archivo.filename)
            listaNombreArchivo = nombreArchivo.split('.')
            extencion = listaNombreArchivo[1].lower()
            
            nuevoNombre = str(idProducto)+ "." + str(extencion)
            archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], nuevoNombre))
            
        mensaje = "Producto Actualizado"
        return redirect("/listaProductos")
        
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje = str(error)
        return render_template("frmActualizarProductos.html")
    
@app.route('/eliminar/<int:idProducto>',methods=['GET'])
def eliminarProducto(idProducto):
    try:        
        producto = Products.query.filter_by(idProducto=idProducto).first()
        db.session.delete(producto)
        db.session.commit()
        mensaje="Producto Eliminado"
        
        producto = Products.query.get(idProducto)
        
        return redirect("/listaProductos")
        
    except exc.SQLAlchemyError as error:
        mensaje=error
        return render_template("listarProductos.html",
                               mensajeEliminar=mensaje)
        
# =================================================================================================

@app.route('/listarProductosJson', methods=['GET'])
def listarProductosJson():
    try:
        listaProductos = Products.query.all()
        listaJosn=[]
        for producto in listaProductos:
            producto = {
                "idProducto": producto.idProducto,
                "proCodigo": producto.proCodigo,
                "proNombre":producto.proNombre,
                "proPrecio":producto.proPrecio,
                "categoria": {
                    "idCategoria": producto.categoria.idCategoria,
                    "catNombre": producto.categoria.catNombre
                }
            }
            listaJosn.append(producto)
        mensaje="Lista de Productos"
    except exc.SQLAlchemyError as error:
        mensaje=error
    return {"mensaje":mensaje, "listaProductos":listaJosn}

@app.route('/consultarProductoJson', methods=['GET'])
def consultarProductoJson():
    try:
      datos = request.get_json(force=True)
      idProducto = int(datos["idProducto"])
      producto = Products.query.get(idProducto)
      productoJson = {
            "idProducto": producto.idProducto,
            "proNombre":producto.proNombre,
            "proPrecio":producto.proPrecio,
            "categoria": {
                "idCategoria": producto.categoria.idCategoria,
                "catNombre": producto.categoria.catNombre
            }
      }
      mensaje="Datos del Producto"
    except exc.SQLAlchemyError as error:
        mensaje = error
    return {"mensaje":mensaje, "producto":productoJson}

@app.route('/agregarProductoJson', methods=['POST'])
def agregarProductoJson():
    estado = False
    try:
        datos = request.get_json(force=True)
        codigo = int(datos['codigo'])
        nombre = datos['nombre']
        precio = int(datos['precio'])
        categoria = int(datos['categoria'])
        producto = Products(proCodigo=codigo,proNombre=nombre,
                            proPrecio=precio,proCategoria=categoria)
        db.session.add(producto)
        db.session.commit()
        mensaje="Producto Agregado Correctamente"
        estado = True
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje="Problemas al registrar"
    return {"mensaje":mensaje,"estado":estado}

@app.route('/eliminarProductoJson', methods=['POST'])
def eliminarProductoJson():
    try:
        estado=False
        datos = request.get_json(force=True)
        idproducto = int(datos["idProducto"])
        producto = Products.query.get(idproducto)
        db.session.delete(producto)
        db.session.commit()
        estado=True
        mensaje="producto Eliminado"
        nombreArchivo = str(idproducto)+".jpg"
        os.remove(os.path.join(app.config["UPLOAD_FOLDER"]+"/"+nombreArchivo))
    except exc.SQLAlchemyError as error:
        db.session.rollback()
        mensaje = "problemas al Elimanr El producto"
    return {"mensaje":mensaje, "estado":estado}

@app.route('/actualizarProductoJson', methods=['POST'])
def actualizarProductoJson():
    try:
        estado = False
        datos = request.get_json(force=True)
        idProducto = int(datos["idProducto"])
        producto = Products.query.get(idProducto)
        producto.proCodigo = int(datos["codigo"])
        producto.proNombre = datos["nombre"]
        producto.proPrecio = int(datos["precio"])
        producto.proCategoria = int(datos["categoria"])
        db.session.commit()
        estado = True
        mensaje = " producto Actualizado"
    except exc.SQLAlchemyError as error:
        db.rollback()
        mensaje = "Problemas al actualizar el Producto"
    return {"mensaje":mensaje,"estado":estado}