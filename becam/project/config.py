
import os

base_dir = os.path.abspath(os.path.dirname(__file__))


class Config:

    MONGOALCHEMY_DATABASE = os.getenv('MONGODB_DATABASE')
    MONGOALCHEMY_CONNECTION_STRING = os.getenv('CONNECTION_STRING')

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
