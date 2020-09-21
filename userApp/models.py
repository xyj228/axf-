from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=64)
    password = models.CharField(max_length=256)
    icon = models.ImageField(upload_to='icons')
    active = models.BooleanField(default=False)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'user'
