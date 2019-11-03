from app import db

import datetime


class User(db.Document):
    identifier = db.StringField()
    name = db.StringField()
    image = db.StringField()

    def count_images(self):
        return ImageUser.query.filter(ImageUser.user == self).count()


class ImageUser(db.Document):
    image = db.StringField()
    created = db.DateTimeField(default=datetime.datetime.now())
    user = db.DocumentField(User)
