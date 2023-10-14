from mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('users_cr_schema').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        # Check if the user already exists based on the email
        existing_user = cls.get_user_by_email(data['email'])
        if existing_user:
            # If a user with the same email exists, return None to indicate the save was not successful.
            return None
        # If no existing user found, proceed to insert the new user.
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        result = connectToMySQL('users_cr_schema').query_db(query, data)
        
        # Return the ID of the newly inserted user.
        return result
    @classmethod
    def get_user_by_email(cls, email):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        data = {'email': email}
        result = connectToMySQL('users_cr_schema').query_db(query, data)
        if result:
            # If a user is found, return a User instance.
            return cls(result[0])
        else:
            # If no user found, return None.
            return None
