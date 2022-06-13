# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Dojo:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    # Now we use class methods to query our database
    @classmethod
    def get_all_dojos(cls):
        query="""
        SELECT * 
        FROM dojos
        ;"""
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append( cls(dojo) )
        return dojos

    @classmethod
    def get_one_dojo(cls, id):
        data={ 'id': id }
        query="""
        SELECT *
        FROM dojos
        WHERE id = %(id)s
        ;"""
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def save(cls, data):
        query="""
        INSERT INTO dojos (name, created_at, updated_at)
        VALUES ( %(name)s, NOW(), NOW() )
        ;"""
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)