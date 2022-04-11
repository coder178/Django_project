from django.db import models
from adminpage.models import Productdetails

from validate.models import Userinfo

# Create your models here.
class userCart(models.Model):
    userid = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    cart_total = models.FloatField()
class cartitems(models.Model):
    cartid = models.IntegerField()
    productid =  models.ForeignKey(Productdetails, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    total = models.FloatField()
class Orderdetails(models.Model):
    userinf = models.ForeignKey(Userinfo, on_delete=models.CASCADE)
    cartid = models.IntegerField()
    payment = models.FloatField()
