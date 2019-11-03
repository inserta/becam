
from flask import Flask
from flask_mongoalchemy import MongoAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api

import os


api = Api()
db = MongoAlchemy()
ma = Marshmallow()


def create_app(script_info=None):
    app = Flask(__name__)
    app_setting = os.getenv("CONFIG")
    app.config.from_object(app_setting)
    db.init_app(app)
    api.init_app(app)
    ma.init_app(app)

    # register own blueprints
    from app.users import users_blueprint

    app.register_blueprint(users_blueprint)

    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db, 'api': api, 'ma': ma}

    return app
