# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Ninja:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    # Now we use class methods to query our database
    @classmethod
    def get_all_ninjas(cls):
        query="""
        SELECT * 
        FROM ninjas
        ;"""
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        ninjas=[]
        for ninja in results:
            ninjas.append( cls(ninja) )
        return ninjas

    @classmethod
    def get_ninjas_for_one_dojo(cls, dojo_id):
        data={'dojo_id': dojo_id}
        query="""
        SELECT *
        FROM ninjas
        WHERE dojo_id= %(dojo_id)s
        ;"""
        these_ninjas=[]
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        for ninja in results:
            these_ninjas.append(ninja)
        return these_ninjas

    @classmethod
    def save(cls,data):
        query="""
        INSERT INTO ninjas
        (first_name, last_name, age, created_at, updated_at, dojo_id)
        VALUES ( %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW(), %(dojo_id)s )
        ;"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)