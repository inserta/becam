from app import ma

from app.users.documents import User, ImageUser

from marshmallow import fields, post_load

import os


class UserSchema(ma.Schema):
    identifier = fields.String()
    name = fields.String()
    image = fields.String()


class ImageUserSchema(ma.Schema):
    image = fields.String()
    created = fields.DateTime()
    user = fields.String()


class AssignImageSchema(ma.Schema):
    user_identifier = fields.String(required=True)
    username = fields.String(required=True)
    image_identifier = fields.String(required=True)

    @post_load
    def make_assign(self, data, **kwargs):
        from app.helpers import FTPHelper
        ftp = FTPHelper()
        ftp.ftp

        user_id = data['user_identifier']
        username = data['username']
        image_id = data['image_identifier']
        image_name = "{}.jpeg".format(image_id)
        if not ftp.exists_file(image_name, "imagenes"):
            return {
                "message": "La imagen no existe",
                "status": 400
            }
        image_url = "{}/{}".format(os.getenv("FTP_DOMAIN"), image_name)

        if User.query.filter(User.identifier == user_id).first():
            user = User.query.filter(User.identifier == user_id).first()
        else:
            user = User(
                identifier=user_id,
                name=username,
                image=image_url
            )
            user.save()
        image = ImageUser(
            image=image_url,
            user=user
        )
        image.save()
        return {
            "data": {
                'user_identifier': user.identifier,
                'username': user.name,
                'count_images': user.count_images()
            },
            "status": 201
        }
