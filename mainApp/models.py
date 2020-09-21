from django.db import models


# Create your models here.


class Wheel(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_wheel'


class Nav(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_nav'


class MustBuy(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()

    class Meta:
        db_table = 'axf_mustbuy'


class MainShow(models.Model):
    img = models.CharField(max_length=64)
    name = models.CharField(max_length=32)
    trackid = models.IntegerField()
    categoryid = models.IntegerField()
    brandname = models.CharField(max_length=32)
    img1 = models.CharField(max_length=64)
    childcid1 = models.IntegerField()
    productid1 = models.IntegerField()
    longname1 = models.CharField(max_length=64)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=64)
    childcid2 = models.IntegerField()
    productid2 = models.IntegerField()
    longname2 = models.CharField(max_length=64)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=64)
    childcid3 = models.IntegerField()
    productid3 = models.IntegerField()
    longname3 = models.CharField(max_length=64)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'


class FoodType(models.Model):
    typeid = models.CharField(max_length=32)
    typename = models.CharField(max_length=64)
    childtypenames = models.CharField(max_length=128)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtype'


class Goods(models.Model):
    productid = models.IntegerField()
    productimg = models.CharField(max_length=32)
    productname = models.CharField(max_length=64)
    productlongname = models.CharField(max_length=64)
    isxf = models.BooleanField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=32)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.IntegerField()
    childcid = models.IntegerField()
    childcidname = models.CharField(max_length=32)
    dealerid = models.IntegerField()
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'


from userApp.models import User


class Cart(models.Model):
    uid = models.ForeignKey(User)
    gid = models.ForeignKey(Goods)
    g_num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

    class Meta:
        db_table = 'cart'
