from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    likes = models.PositiveBigIntegerField(default=8)

class User(models.Model):
    pass
