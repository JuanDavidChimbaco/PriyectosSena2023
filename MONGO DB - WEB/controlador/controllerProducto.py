from app import app,productos
from flask import Flask, request,render_template,redirect
import pymongo
import traceback
from werkzeug.utils import secure_filename
import os
from bson.objectid import ObjectId

@app.route('/')
def inicio():
    listaProductos=listarProductos()
    print(type(listaProductos))
    return render_template("listarProductos.html",
                           listaProductos=listaProductos)

    
@app.route('/vistaAgregarProducto')
def vistaAgregarProducto():
    producto={}
    return render_template("frmAgregarProducto.html",producto=producto)
           
@app.route('/agregarProducto',methods=['POST'])
def agregarProducto():
    try:
        codigo = int(request.form['txtCodigo'])
        nombre = request.form['txtNombre']
        categoria = request.form['cbCategoria']
        precio = int(request.form['txtPrecio'])
        
        # datos de la imagen
        archivo = request.files["fileFoto"]
        extencion = ""
        if archivo:
            nombreArchivo = secure_filename(archivo.filename)
            listaNombreArchivo = nombreArchivo.split('.')
            extencion = listaNombreArchivo[1].lower()
        else:
            print("No imagen")
        
        producto = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        
        existe = consultarProductoCodigo(codigo)
        if(existe):
            mensaje="Ya existe producto con ese código."
            return render_template('frmAgregarProducto.html', producto=producto,mensajeAgregar=mensaje)
            
        else:
            resultado = productos.insert_one(producto)
            mensaje="Producto agregado correctamente."
            print(extencion)
            #obtener el id del producto que se acaba de insertar
            idProducto = resultado.inserted_id
            #nuevoNombre = (f"{idProducto}.{extencion}")
            nuevoNombre = str(idProducto)+ "." + str(extencion)
            print(nuevoNombre)
            folder = app.config['UPLOAD_FOLDER']
            print(folder)
            path = os.path.join(folder,nuevoNombre)
            print(path)
            archivo.save(path)
            
            listaProductos=listarProductos()
            return render_template("listarProductos.html",
                               mensajeAgregar=mensaje,
                               listaProductos=listaProductos)
            
    except Exception as error:
        traceback.print_exc()
        mensaje= str(error)
        return render_template('frmAgregarProducto.html', producto=producto, mensaje=mensaje)
              
def consultarProductoCodigo(codigo):
    try:
        consulta = {"codigo": codigo}
        producto = productos.find_one(consulta)
        if(producto is not None):
            return True
        else:
            return False
        
    except pymongo.errors as error:
        mensaje=error
        return False and mensaje

@app.route("/vistaActualizarProducto/<int:codigo>", methods=["GET"])        
def vistaActualizarProducto(codigo):
    try:
        criterio = {"codigo": codigo }
        producto = productos.find_one(criterio)
        if (producto):
            print(producto)
            mensaje="producto encontrado"
            return render_template('frmActualizarProducto.html', producto=producto, mensajeActualizar=mensaje)
        else:
            mensaje="producto No encontrado"
    
    except pymongo.errors as error:
        traceback.print_exc()
        mensaje=str(error)
        return render_template('frmActualizarProducto.html', producto=datosActualizar, mensajeActualizar=mensaje)

@app.route("/actualizarProducto", methods=['POST'])
def actualizarProducto():
    try:
        codigo = int(request.form['txtCodigo'])
        nombre = request.form['txtNombre']
        categoria = request.form['cbCategoria']
        precio = int(request.form['txtPrecio'])
        
        datosActualizar = {
            "codigo": codigo,
            "nombre": nombre,
            "categoria": categoria,
            "precio": precio
        }
        criterio = {"codigo":codigo}
        consulta = { "$set" : datosActualizar}
        resultado = productos.update_one(criterio,consulta)
        if (resultado):
            print(resultado)
            mensaje="Producto actualizado."
            listaProductos=listarProductos()
            return render_template("listarProductos.html",
                                mensajeActualizar=mensaje,
                                listaProductos=listaProductos)
        else:
            mensaje="Producto NO actualizado."
            listaProductos=listarProductos()
            return render_template("listarProductos.html",
                                mensajeActualizar=mensaje,
                                listaProductos=listaProductos)
        
    except pymongo.errors as error:
        traceback.print_exc()
        mensaje = str(error)
        return render_template('frmActualizarProducto.html', producto=datosActualizar, mensajeActualizar=mensaje)

@app.route('/eliminar/<int:codigo>',methods=['GET'])
def eliminarProducto(codigo):
    try:        
        consulta = {"codigo":codigo}
        productos.delete_one(consulta)
        mensaje="Producto Eliminado"
        
        """return mensaje and redirect("/")"""
        
        listaProductos=listarProductos()
        return render_template("listarProductos.html",
                               mensajeEliminar=mensaje,
                               listaProductos=listaProductos)
        
    except pymongo.errors as error:
        mensaje=error
        listaProductos=listarProductos()
        return render_template("listarProductos.html",
                               mensajeEliminar=mensaje,
                               listaProductos=listaProductos)
        
def listarProductos():
    try:
        listarProductos = productos.find()
        return listarProductos
        
    except pymongo.errors as error:
        mensajeLista = error
        return mensajeLista