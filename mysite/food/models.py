from django.db import models

# defines a structure in which database is framed
# Create your models here.
# A model is created using a class

class Item(models.Model):

    def __str__(self):
        return self.item_name

    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()

    