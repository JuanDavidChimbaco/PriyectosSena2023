from flask import Flask, render_template
from modelo.tienda import Tienda

app = Flask(__name__)
tienda = Tienda()

@app.route("/")
def inicio():
    return render_template("inicio.html")

from controlador.controllerProducto import *
from controlador.controllerCliente import *
from controlador.controllerVenta import *


if __name__=="__main__":
    app.run(port=3000,debug=True)