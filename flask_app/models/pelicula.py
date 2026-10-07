#TODAS LAS CLASES IMPORTAN MYSQLCONNECTION
from flask_app.config.mysqlconnection import connectToMySQL

class Pelicula:

    def __init__(self, data):
        self.id = data.get('id')
        self.nombre = data.get('nombre')
        self.director = data.get('director')
        self.fecha_estreno = data.get('fecha_estreno')
        self.sinopsis = data.get('sinopsis')
        self.created_at = data.get('created_at')
        self.updated_at = data.get('updated_at')
        self.usuario_id = data.get('usuario_id')

        #para guardar un registro
        @classmethod
        def save(cls, data):
            query = "INSERT INTO peliculas (nombre, director, fecha_estreno, sinopsis, created_at, updated_at, usuario_id) VALUES (%(nombre)s, %(director)s, %(fecha_estreno)s, %(sinopsis)s, NOW() NOW()), %(usuario_id)s"
            return connectToMySQL ('CinePediarepaso').query_db(query, data)


        #Metodo para ver todos los registros
        @classmethod
        def get_all(cls):
            query = "SELECT = FROM peliculas"
            peliculas_en_bd = connectToMySQL('CinePediarepaso').query_db(query)
            #Lista vacia de usuarios se llena con class usuarios
            peliculas = []
            #por cada usuario que encuentre en usuarios_db
            for peliculas in peliculas_en_bd:
                #voy a crear una instancia de la clase Usuario al final de la lista usuarios
                peliculas.append(cls(pelicula))
            return peliculas

        #Metodo para ver 1 registro
        @classmethod
        def get_one(cls,datos):
            query = "SELECT * FROM peliculas WHERE id = %(id)s;"
            peliculas_en_db = connectToMySQL('CinePediarepaso').query_db(query,datos)

        #Metodo para editar registro
        @classmethod
        def update(cls, datos):
            query = "UPDATE peliculas SET nombre=%(nombre)s, director=%(director)s, fecha_estreno=%(fecha_estreno)s, sinopsis=%(sinopsis)s, updated_at=NOW(), %(usuario_id)s WHERE id = %(id)s;"
            return connectToMySQL('CinePediarepaso').query_db(query, datos)

        #Metodo para eliminar 1 registro
        @classmethod
        def delete(cls, datos):
            query = "DELETE FROM peliculas WHERE id = %(id)s;"
            return connectToMySQL('CinePediarepaso').query_db(query, datos)


