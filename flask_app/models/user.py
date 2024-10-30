from flask_app.config.mysqlconnection import connectToMySQL
from pprint import pprint


class User:
    DB = "users_schema"

    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, form_data):
        """Inserts a user user into the database"""

        query = """
        INSERT INTO users(first_name, last_name, email)
        VALUES (%(first_name)s,%(last_name)s, %(email)s);"""

        user_id = connectToMySQL(cls.DB).query_db(query, form_data)
        return user_id

    @classmethod
    def get_all(cls):
        """Final all users in the database"""
        query = "SELECT * FROM users;"
        list_of_dicts = connectToMySQL(cls.DB).query_db(query)
        pprint(list_of_dicts)

        users = []
        for each_dict in list_of_dicts:
            user = User(each_dict)
            users.append(user)
        return users

    @classmethod
    def update_user(cls, form_data):
        """ updates a user into the database"""

        query = """
        UPDATE users
        SET
        first_name = %(first_name)s,
        last_name = %(last_name)s,
        email = %(email)s
        WHERE id = %(user_id)s;
        """
        return connectToMySQL(cls.DB).query_db(query, form_data)

    @classmethod
    def edit_user(cls,user_id):
        """ edit the user by ID """

        query = """ UPDATE user WHERE id = %(user_id)s;"""
        data = {"user_id": user_id}

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def delete_user(cls, user_id):
        """ delete a user from the database"""

        query = """
        DELETE FROM users
        WHERE id = %(user_id)s;
        """

        data = {"user_id":user_id}

        return connectToMySQL(cls.DB).query_db(query, data)

    @classmethod
    def find_by_id(cls, user_id):
        """ Finds the user in the database"""

        query = """
        SELECT * FROM users
        WHERE id = %(user_id)s;
        """

        data = {"user_id":user_id}
        one_user = connectToMySQL(cls.DB).query_db(query, data)
        user = User(one_user[0])
        return user
