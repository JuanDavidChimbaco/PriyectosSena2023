from flask import Flask , request, render_template
import yagmail
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']="./"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/enviarCorreo', methods=['POST'])
def enviarCorreo():
    try:
        # tomar los datos del formulario 
        destinatario = request.form['txtDestinatario']
        remitente = request.form['txtOrigen']
        asunto = request.form['txtAsunto']
        textoMensaje = request.form['txtMensaje']
        
        # subir un archivo y guardarlo en la raiz
        archivo = request.files['fileAnexo']
        nombreArchivo = secure_filename(archivo.filename)
        archivo.save(os.path.join(app.config['UPLOAD_FOLDER'],nombreArchivo))
        
        # creo el correo que sera el remitente
        email = yagmail.SMTP('dajun318@gmail.com',open('password').read(),encoding='utf8')
        # correo de desinatario 
        # el 'to' puede ser una lista
        email.send(to=destinatario, subject=asunto,contents=textoMensaje, attachments=nombreArchivo)
        mensajeResultado = "Correo Enviado"
        # eliminar el archivo del servidor
        os.remove(os.path.join(app.config['UPLOAD_FOLDER']+"/"+nombreArchivo))
        
    except Exception as error:
        mensajeResultado = error
        
    return render_template('index.html', mensaje=mensajeResultado)


if __name__ == '__main__':
    app.run(debug=True , port=8080)