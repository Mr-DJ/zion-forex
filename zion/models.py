from locale import currency
from unicodedata import name
from django.db import models

# Create your models here.
class Currency(models.Model):
    currency_name = models.CharField(max_length=100)
    buy_price = models.FloatField()
    sell_price = models.FloatField()

    def __str__(self):
        return self.currency_name