import pymysql as mysql
from flask import Flask, request,render_template, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static/img' 
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

user = "root"
passwordUser = ""
baseDatos = "peliculaspython"
host="localhost"

mysqlConnection = mysql.Connect(host=host,user=user,passwd=passwordUser,db=baseDatos)
cursor = mysqlConnection.cursor()

@app.route("/")
def inicio():
    listaPeliculas  = listarPeliculas()
    listaGeneros = listarGeneros()
    return render_template("frmAgregarPeliculas.html", listaPeliculas = listaPeliculas, listaGeneros = listaGeneros)

    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        return False

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
           
@app.route("/agregarPelicula" , methods=["POST"])
def agregarPelicula():
    mensaje,estado ="",False
    try:
        codigo = int(request.form["txtCodigo"])
        titulo = request.form["txtTitulo"]
        duracion = int(request.form["txtDuracion"])
        director = request.form["txtDirector"]
        fechaLanzamiento = request.form["txtFechaLanzamiento"]
        resumen = request.form["txtResumen"]
        genero = request.form["cbGenero"]
        pelicula = (codigo,titulo,duracion,director,fechaLanzamiento,resumen,genero)
        
        cursor = mysqlConnection.cursor()
        consulta = "INSERT INTO peliculas VALUES(null,%s,%s,%s,%s,%s,%s,%s)"
        resultado = cursor.execute(consulta,pelicula)
        
        #por defecto el commit esta desactivado,entonces toca agregarlo y se hace cuando se actualiza la base de datos. 
        mysqlConnection.commit() 
        
        if (cursor.rowcount==1):
            archivo = request.files["fileFoto"]
            if archivo and allowed_file(archivo.filename):
                fileName = secure_filename(archivo.filename)
                listFileName = fileName.split('.', 1)
                extension = listFileName[1].lower()

                consulta = "select max(idPeliculas) from peliculas"
                cursor.execute(consulta)
                last_id = cursor.fetchone()[0]

                newName = f"{last_id}.{extension}"

                archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
            
            mensaje="Pelicula Agregada"
            estado = True
    except mysqlConnection.Error as error:
        mysqlConnection.rollback()
        mensaje = f"Problemas al agregar Peliculas, Error {error}"
    listaPeliculas = listarPeliculas() 
    return jsonify({"estado":estado,"mensaje":mensaje ,"listaPeliculas":listaPeliculas})

def listarPeliculas():
    try:
        cursor = mysqlConnection.cursor()
        consulta = "select peliculas.*, generos.genNombre from peliculas inner join generos on pelGenero = idGenero"
        resultado = cursor.execute(consulta)
        return cursor.fetchall()
    except Exception as error:
        mensaje = error
        
def listarGeneros():
    try:
        cursor = mysqlConnection.cursor()
        consulta = "select * from generos"
        resultado = cursor.execute(consulta)
        return cursor.fetchall()
    except Exception as error:
        mensaje = error

@app.route("/consultarPorCodigo" , methods=["POST"])
def consultarPorCodigo():
    peliculaConsultada = None
    mensaje=""
    try:
        #datos = request.json
        codigo = int(request.form["codigo"])
        #codigo = int(datos["codigo"])
        cursor = mysqlConnection.cursor()
        consulta = "SELECT peliculas.* ,generos.genNombre FROM peliculas join generos on peliculas.pelGenero WHERE pelCodigo = %s AND idGenero = pelGenero" #los parametros siempre se envian en una tupla
        parametro = (codigo,)#esto es una tupla con 1 solo valor
        resultado = cursor.execute(consulta,parametro)
        if (cursor.rowcount>0):
            peliculaConsultada = cursor.fetchone()
            print(peliculaConsultada)
        else:
            mensaje ="No existe pelicula con ese Codigo"
    except Exception as error:
        mensaje = error
    print(peliculaConsultada)
    return jsonify({
        "peliculaConsultada":peliculaConsultada,
        "mensaje":mensaje
        })

@app.route("/actualizar" , methods=["POST"])
def actualizar():
    mensaje = ""
    estado = False
    listaPeliculas = None
    try:
        codigo = int(request.form["txtCodigo"])
        titulo = request.form["txtTitulo"]
        duracion = int(request.form["txtDuracion"])
        director = request.form["txtDirector"]
        fechaLanzamiento = request.form["txtFechaLanzamiento"]
        resumen = request.form["txtResumen"]
        genero = request.form["cbGenero"]
        id = int(request.form["idPelicula"])
        
        peliculaActualizada = (codigo, titulo, duracion, director, fechaLanzamiento, resumen, genero ,id)
        consulta = "UPDATE `peliculas` SET pelCodigo = %s, pelTitulo = %s , pelDuracion = %s , pelDirector = %s , pelFechaLanzamiento = %s, pelResumen = %s, pelGenero = %s WHERE idPeliculas = %s"

        resultado = cursor.execute(consulta,peliculaActualizada)
        mysqlConnection.commit()
                
        if (cursor.rowcount > 0):
            
            archivo = request.files["fileFoto"]
            if archivo and allowed_file(archivo.filename):
                fileName = secure_filename(archivo.filename)
                listFileName = fileName.split('.', 1)
                extension = listFileName[1].lower()
                newName = f"{id}.{extension}"
                archivo.save(os.path.join(app.config['UPLOAD_FOLDER'], newName))
            estado  = True
            mensaje = "Pelicula Actualizada Correctamente"
            
    except Exception as e:
        mysqlConnection.rollback()
        mensaje = e
    listaPeliculas = listarPeliculas()
    return jsonify({
        "estado":estado,
        "mensaje":mensaje,
        "listaPeliculas":listaPeliculas})
    
@app.route("/eliminar", methods=["POST"])
def eliminar():
    mensaje,estado = "",False
    try:
        datos = request.json
        idPelicula = int(datos["idPelicula"])
        
        cursor = mysqlConnection.cursor()
        
        consulta = "DELETE FROM `peliculas` WHERE  `idPeliculas`=%s"
        parametros = (idPelicula,)
        
        resultado = cursor.execute(consulta,parametros)
        mysqlConnection.commit()
        
        if (cursor.rowcount > 0):
            estado=True
            mensaje="Pelicula eliminada correctamente"
                
    except Exception as error:
        mysqlConnection.rollback()
        mensaje = error
        
    listaPeliculas = listarPeliculas()
    return jsonify({
        "estado":estado,
        "mensaje":mensaje,
        "listaPeliculas":listaPeliculas})
 
if __name__ == "__main__":
    app.run(port=3000,debug=True)