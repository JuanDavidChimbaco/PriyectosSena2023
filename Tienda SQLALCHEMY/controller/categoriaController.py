from app import app
from model.categoria import *
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc

@app.route('/agregarCategoria', methods=['GET', 'POST'])
def agregarCategoria():
    try:
        nombre = (request.form['txtCategoria']).upper()
        categoria = Category(catNombre=nombre)
        db.session.add(categoria)
        db.session.commit()
        mensaje ="Categoria Agreggada Correctamente"
    except exc.SQLAlchemyError as ex:
        db.session.rollback()
        mensaje = str(ex)
    return render_template('agregarCategoria.html',mensaje=mensaje)