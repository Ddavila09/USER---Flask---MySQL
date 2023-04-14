from mysqlconnection import connectToMySQL

DATABASE = "users"


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
                new_user = User(dict)
                users.append(new_user)
                
        return users
    
    @classmethod
    def create(cls, data):

        query = "INSERT INTO users_schema (first_name, last_name, email) VALUES(%(first_name)s, %(last_name)s, %(email)s)"
        
        return connectToMySQL(DATABASE).query_db(query, data)