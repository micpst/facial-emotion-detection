from os import getenv


class Config:
    """
    Base configuration
    """
    SECRET_KEY = getenv('SECRET_KEY')


class ProductionConfig(Config):
    """
    Production configuration
    """


class DevelopmentConfig(Config):
    """
    Development configuration
    """


class TestingConfig(Config):
    """
    Testing configuration
    """
    TESTING = True
