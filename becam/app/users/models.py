# -*- encoding: utf-8 -*-
from django.contrib.auth.models import User
from django.db import models


class ImageUser(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)
    image_identifier = models.CharField(max_length=100, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField()

    class Meta:
        verbose_name_plural = u"Imágnes de usuario"

    def __str__(self):
        return "{}-{}".format(self.user, self.image_identifier)
