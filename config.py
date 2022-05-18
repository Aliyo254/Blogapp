from distutils.debug import DEBUG
import os

class Config:

    '''
    class config
    '''
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://alinur:admin@localhost/blog'
    SECRET_KEY=os.environ.get("SECRET_KEY")


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI=os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URI.startswith('postgres://'): 
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace('postgres://','postgresql://',1)

   


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alinur:admin@localhost/blog_test'

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    DEBUG=True

config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}