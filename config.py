import os

class Config:

    '''
    class config
    '''


class ProdConfig(Config):
    '''
    Production  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''




    SECRET_KEY='1234'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://alinur:admin@localhost/blog'




class TestConfig(Config):
    '''
    test configurations
    '''

class DevConfig(Config):
    '''
    Development  configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True

config_options = {
'development':DevConfig,
'test':TestConfig,
'production':ProdConfig
}