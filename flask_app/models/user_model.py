from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def __repr__(self):
        return f"USER: {self.first_name}"

    @classmethod
    def get_all(cls):

        query = "SELECT * FROM users_schema"

        results = connectToMySQL(DATABASE).query_db(query)

        users = []

        if results:
            for dict in results:
                new_user = cls(dict)
                users.append(new_user)

        return users

    @classmethod
    def get_one(cls, id):

        data = {
            "id": id,
        }

        query = """
     
            SELECT * FROM users_schema
            WHERE id = %(id)s;
     
     
         """
        results = connectToMySQL(DATABASE).query_db(query, data)
        person = cls(results[0])

        return person

    @classmethod
    def save(cls, data):
     
        query = """
        
        UPDATE users_schema
        SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s
        WHERE
        id = %(id)s;
        
        """

        connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def create(cls, data):

        query = "INSERT INTO users_schema (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s)"

        return connectToMySQL(DATABASE).query_db(query, data)
    
    
    
    @classmethod
    def delete(cls, id):
        
        data = {
            "id": id,
        }
    
        query = """
        
        DELETE FROM users_schema
        WHERE id = %(id)s;
        
        """
        connectToMySQL(DATABASE).query_db(query, data)