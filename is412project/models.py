from django.db import models


class Item(models.Model):
    item_id = models.CharField(max_length=200)
    item_name = models.CharField(max_length=200)
    item_description = models.IntegerField() 
    item_quantity = models.IntegerField()
    item_price = models.IntegerField()



