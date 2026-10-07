from flask_app import app
from flask import render_template

@app.route("/")
def inicio():
    return render_template('index.html')


#registro crear usuario
@app.route("/crear_usuario")
def crear_usuario():
    return



#inicio de sesion


#cerrrar sesion