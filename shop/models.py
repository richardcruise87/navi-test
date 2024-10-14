from django.db import models

class ShopName(models.Model):
    name = models.CharField(max_length=200)
    date_opened = models.DateTimeField("date opened")