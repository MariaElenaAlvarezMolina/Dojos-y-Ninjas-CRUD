from flask_app.config.mysqlconnection import connectToMySQL
from .ninjas import Ninja

class Dojo:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = []


    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO dojos (nombre) VALUES (%(nombre)s)"
        result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, formulario)
        return result

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query)
        dojos = []
        for d in results:
            dojos.append(cls(d))
        return dojos

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s"
        results = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, data)
        dojo = cls(results[0])
        
        for row in results:
            ninja = {
                'id': row['ninjas.id'],
                'nombre': row['ninjas.nombre'],
                'apellido': row['apellido'],
                'edad': row['edad'],
                'created_at': row['created_at'],
                'updated_at': row['updated_at'],
                'dojo_id': row['dojo_id']
            }
            instancia_ninja = Ninja(ninja)
            dojo.ninjas.append(instancia_ninja)
        
        return dojo