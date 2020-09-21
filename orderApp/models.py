from django.db import models

# Create your models here.
from mainApp.models import Goods
from userApp.models import User


class Order(models.Model):
    o_user = models.ForeignKey(User)
    o_creattime = models.DateTimeField(auto_now_add=True)
    o_totalprice = models.FloatField()

    class Meta:
        db_table = 'order'


class orderGoods(models.Model):
    og_order = models.ForeignKey(Order)
    og_goods = models.ForeignKey(Goods)
    og_goods_num = models.IntegerField()

    class Meta:
        db_table = 'order_goods'
