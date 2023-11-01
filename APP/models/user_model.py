from abc import ABC
from datetime import datetime
from APP import getCursor
import bcrypt
from flask_login import UserMixin, LoginManager, login_user, logout_user, current_user

class User (UserMixin):
    def __init__(self, userID:int, username: str, password: str, role: str, name: str, phone: int, address: str, email:str):
        self.__userID = userID
        self.__username = username
        self.__password = password
        self.__role = role
        self.__name = name
        self.__phone = phone
        self.__address = address
        self.__email = email
    
    @property
    def userID(self):
        return self.__userID
    
    def get_id(self):
        return str(self.__userID)
    
    @property
    def username(self):
        return self.__username
    
    @username.setter
    def username(self, username):
        self.__username= username
    
    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        self.__password = password

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, role):
        self.__role = role

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone):
        self.__phone = phone

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        self.__email = email

    # Returns True if the user is authenticated.
    def is_authenticated(self):
        return True

    @staticmethod
    def get_user(user_id):
        connection = getCursor()
        connection.execute("SELECT * FROM user WHERE userID = %s;", (user_id,))
        user_data = connection.fetchone()

        if user_data is not None:
            # Create a User object and assign values from the database
            user = User(
                userID=user_data[0],
                username=user_data[1],
                password=user_data[2],
                role=user_data[3],
                name=user_data[4],
                phone=user_data[5],
                address=user_data[6],
                email=user_data[7]
            )
            return user
        else:
            return None

    @classmethod
    def login(cls, username, password):
        connection = getCursor()
        connection.execute("SELECT * FROM user WHERE username = %s;", (username,))
        user = connection.fetchone()

        if user and bcrypt.checkpw(password.encode('utf-8'), user[2].encode('utf-8')):
            return cls(
                userID=user[0],
                username=user[1],
                password=user[2],
                role=user[3],
                name=user[4],
                phone=user[5],
                address=user[6],
                email=user[7]
            )

        return None

    @staticmethod
    def check_username_exist(username):
        connection = getCursor()
        connection.execute("""SELECT username FROM username WHERE username = %s;""", (username,))
        existing_username = connection.fetchone()

        if existing_username is not None:
            return True #if user exists, return True, not exists return False
    
    def save_to_database(self):
        hashedp = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt())
        connection = getCursor()
        insert_query = "INSERT INTO user (username, password, role, name, phone, address, email) VALUES (%s, %s,'customer', %s, %s, %s, %s)"
        values = self.username, hashedp, self.name, self.phone, self.address, self.email
        
        try:
            connection.execute(insert_query, values)
            return True
        except Exception as ex:
            print(f"Error while saving to database: {ex}")
            return False

    @staticmethod
    def logout():
        logout_user()

    @classmethod
    def create_user(cls, user):
        # Make sure the user object is properly initialized with necessary attributes
        connection = getCursor()
        insert_query = """
            INSERT INTO user (username, password, role, name, phone, address, email)
            VALUES (%s, %s, 'customer', %s, %s, %s, %s)
        """
        values = (user.username, user.password, user.name, user.phone, user.address, user.email)

        try:
            connection.execute(insert_query, values)
            return True
        except Exception as ex:
            print(f"Error while creating and saving user to the database: {ex}")
            return None
        
    
    @classmethod
    def get_all_usernames(cls):
        connection = getCursor()
        query = "SELECT username FROM user"
        connection.execute(query)
        results = connection.fetchall()

        # Extract usernames from the query results
        usernames = [result[0] for result in results]

        return usernames