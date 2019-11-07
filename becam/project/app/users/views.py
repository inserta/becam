# --*-- blueprint --*--
from marshmallow import ValidationError

from . import users_blueprint

from flask import request

# --*-- flask-restful --*--
from flask_restful import fields, Resource, Api

from app.users.documents import User, ImageUser
from app.users.schemas import AssignImageSchema, UserSchema, ImageUserSchema

VERSION_API = "/api/v1/"

api = Api(users_blueprint)


assignimage_schema = AssignImageSchema()


class UserResource(Resource):

    def get(self):
        return {
            'users': UserSchema(many=True).dump(User.query.all()),
        }, 200

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message':  'No input data provided'}, 400

        try:
            data = assignimage_schema.load(json_data)
            if data['status'] == 201:
                return data['data'], 201
            elif data['status'] == 400:
                return data['message'], 400
        except ValidationError as err:
            return err.messages


class ImaegeResource(Resource):

    def get(self):
        return {
            'images': ImageUserSchema(many=True).dump(ImageUser.query.all())
        }


api.add_resource(UserResource, VERSION_API + 'users')
api.add_resource(ImaegeResource, VERSION_API + 'images')
