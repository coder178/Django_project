from django.db import models

# Create your models here.
class Productdetails(models.Model):
    productname = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    stock = models.IntegerField(default=25)
    productimg = models.ImageField(upload_to = "productimgs")