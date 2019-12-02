class Config(object):
    # Set port for flask to listen on
    PORT = 5000

    # SQLalchemy
    # Save DB in memory
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"

    # secret key
    SECRET_KEY = 'super_secret_key'

class DevelopmentConfig(Config):
    # DEBUG mode
    DEBUG = True

    # Set bind
    HOST = '127.0.0.1'
    

class DockerConfig(Config):
    # DEBUG mode
    DEBUG = False

    # Set bind
    HOST = '0.0.0.0'