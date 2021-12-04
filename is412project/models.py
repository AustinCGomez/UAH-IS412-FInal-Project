from django.db import models



#This will create our database for the item system 
class Item(models.Model):
    item_id = models.IntegerField(default = 0)
    item_name = models.CharField(max_length = 200)
    item_description = models.CharField(max_length = 200)
    item_quantity = models.IntegerField(default = 0)
    item_price = models.IntegerField(default = 0)

    def __str__(self):
        return self.item_name
