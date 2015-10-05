from django.db import models


class Air(models.Model):
    uuid = models.IntegerField()
    pm25 = models.FloatField()
    pub_date = models.DateTimeField()
# Create your models here.
