import configparser

def read_db_config(filename):
    config = configparser.ConfigParser()
    config.read(filename)

    host = config.get('database', 'host')
    user = config.get('database', 'user')
    password = config.get('database', 'password')
    database = config.get('database', 'database')

    db_config = {
        'host': host,
        'user': user,
        'password': password,
        'database': database
    }

    return db_config
