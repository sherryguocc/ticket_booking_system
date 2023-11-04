from APP import connect
from flask import Flask
from flask_login import  LoginManager
from config import Config
import mysql.connector

# creates an instance of the Flask class for the application.
app = Flask(__name__)

# loads the configuration settings from the Config class into your Flask application.
app.config.from_object(Config)

dbconn = None
connection = None

# creates an instance of the LoginManager class.
login_manager = LoginManager()
login_manager.init_app(app)

# establishes a connection to the MySQL database using the parameters defined in the connect module.
# It then returns a cursor object which can be used to execute SQL commands.
def getCursor():
    global dbconn
    global connection
    connection = mysql.connector.connect(user=connect.dbuser, \
    password=connect.dbpass, host=connect.dbhost, \
    database=connect.dbname, autocommit=True)
    dbconn = connection.cursor()
    return dbconn

# Import various modules from APP folder
from APP.home_view import bp as home_bp
from APP.admin_view import admin as admin_bp
from APP.customer_view import customer as customer_bp
from APP.staff_view import staff as staff_bp

app.register_blueprint(home_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(customer_bp)
app.register_blueprint(staff_bp)