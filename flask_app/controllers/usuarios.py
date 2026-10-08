from flask_app import app
from flask import render_template
from flask_app.models.usuario import Usuario
from flask_bcrypt import Bcrypt #Importamos bycrpt

@app.route("/")
def inicio():
    return render_template('index.html')


#registro crear usuario
@app.route("/crear_usuario", methods=['POST'])
def crear_usuario():
    if not Usuario.validar_usuario(reques.form):
        flash("El correo es obligatorio", "correo") #La categoría es "correo"
        return redirect('/')

    #para agregar un nuevo usuario lo primero que debo hacer es recuperar la informacion desde el formulario 
    #para hacer eso necesitamo el request.form
    #(%(nombre)s, %(apellido)s, %(email)s, %(password)s
    datos_usuario_registros = {
        "nombre": request.form ['nombre'],
        "apellido": request.form ['apellido'],
        "email": request.form ['email'],
        "password": pass_hasheado
        
    }



    return 



#inicio de sesion


#cerrrar sesion