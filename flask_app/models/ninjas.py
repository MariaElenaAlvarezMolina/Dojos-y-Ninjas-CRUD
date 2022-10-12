from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.edad = data['edad']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

    
    @classmethod
    def save(cls, formulario):
        query = "INSERT INTO ninjas (nombre, apellido, edad, dojo_id) VALUES (%(nombre)s, %(apellido)s, %(edad)s, %(dojo_id)s)"
        result = connectToMySQL('esquema_dojos_y_ninjas').query_db(query, formulario)
        return result