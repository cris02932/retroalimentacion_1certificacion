#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL
import re   # Importamos expresiones regulares
from flask import flash

# Objeto de expresión regular que usaremos para validar

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+.[a-zA-Z]+$')


class Usuario:

    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.apellido = data.get('apellido')
        self.email = data.get('email')
        self.password = data.get('password')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')

        #para guardar un registro
        @classmethod
        def save(cls, data):
            query = "INSERT INTO usuarios (nombre, apellido, email, password, created_at, updated_at) VALUES (%(nombre)s, %(apellido)s, %(email)s, %(password)s, NOW() NOW())"
            return connectToMySQL ('CinePediarepaso').query_db(query, data)


        #Metodo para ver todos los registros
        @classmethod
        def get_all(cls):
            query = "SELECT = FROM usuarios"
            usuarios_en_bd = connectToMySQL('CinePediarepaso').query_db(query)
            #Lista vacia de usuarios se llena con class usuarios
            usuarios = []
            #por cada usuario que encuentre en usuarios_db
            for usuario in usuarios_en_bd:
                #voy a crear una instancia de la clase Usuario al final de la lista usuarios
                usuarios.append(cls(usuario))
            return usuarios

        #Metodo para ver 1 registro
        @classmethod
        def get_one(cls,datos):
            query = "SELECT * FROM usuarios WHERE id = %(id)s;"
            usuario_en_db = connectToMySQL('CinePediarepaso').query_db(query,datos)

        #Metodo para editar registro
        @classmethod
        def update(cls, datos):
            query = "UPDATE usuarios SET nombre=%(nombre)s, apellido=%(apellido)s, email=%(email)s, password=%(password)s WHERE id = %(id)s;"
            return connectToMySQL('CinePediarepaso').query_db(query, datos)

        #Metodo para eliminar 1 registro
        @classmethod
        def delete(cls, datos):
            query = "DELETE FROM usuarios WHERE id = %(id)s;"
            return connectToMySQL('CinePediarepaso').query_db(query, datos)



        @classmethod
        def get_by_email(cls, datos):
            query = "SELECT * FROM usuarios WHERE id = %(id)s;"
            usuario_en_db = connectToMySQL('CinePediarepaso').query_db(query,datos)
            return cls(usuario_en_db[0])


        #Usamos metodo estatico para validar los formularios
        @staticmethod
        def validar_usuario( usuario ):

            es_valido = True

            #Revisa si el campo coincide con el patrón

            if not EMAIL_REGEX.match(usuario['email']):

                flash("E-mail inválido")

                es_valido = False
            if len(usuario['nombre']) <=2:
                flash("El nombre del Usuario necesita al menos 2 caracteres", "usuario")
                es_valido = False
            if len(Usuario['apellido']) <=2:
                flash("El apellido del Usuario necesita al menos 2 caracteres", "usuario")
                es_valido = False
            if len(Usuario['password']) == Usuario['password_conf']:
                flash("La contraseña no coincide con la confirmacion")
                es_valido = False
            #Falta validacion de contraseña = confirmacion de contraseña

            return es_valido

        


        @classmethod
        def validar_login(usuario):

            es_valido = True

            if not Usuario.get_by_email({'email':Usuario['email']}):
                flash('el correo no se encuetra en la base de datos')


