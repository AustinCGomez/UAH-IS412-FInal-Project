from django.db import models
from is412project.models import Item

# Create your models here.
#This will create our database for the item system 
class Checkout(models.Model):
    itemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    itemQuan = models.IntegerField(default = 0)
    fnameandlname = models.CharField(max_length = 200)
    address = models.CharField(max_length = 200)
    phoneNum = models.IntegerField(max_length = 200)
    zipCode = models.IntegerField(default = 0)
    ccard = models.IntegerField(default = 0)

    def __str__(self):
        return self.address


