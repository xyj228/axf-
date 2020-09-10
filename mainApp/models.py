from django.db import models


# Create your models here.


class Wheel(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'
