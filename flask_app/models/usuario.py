#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL

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


