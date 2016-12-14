from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from  mixins import HasChangedMixin
# Create your models here.


"""Model to define Items"""
class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    product_code = models.CharField(max_length=25,unique=True)
    product_name = models.CharField(max_length=25)


    def __str__(self):
        return self.product_name

"""Model to define Items with details"""
class Variant(models.Model,HasChangedMixin):
    variant_id = models.AutoField(primary_key=True)
    item_code = models.ForeignKey(Item,on_delete=models.CASCADE)
    cost = models.FloatField()
    quantity = models.IntegerField()
    color = models.CharField(max_length=20)

"""Model to define Product characteristics of a Item Variant"""

class Option(models.Model):
    variant_id = models.ForeignKey(Variant)
    option_field = models.CharField(max_length=20)
    option_value = models.CharField(max_length=50)


"""Model to define to log User Actions"""
class UserActionLog(models.Model):
    action_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User)
    user_action = models.CharField(max_length=10)
    log_msg = models.CharField(max_length=60)
    time = models.DateTimeField(auto_now_add=True)