import datetime

from django.db import models
from django.utils import timezone


class Type(models.Model):
    type_text = models.CharField(max_length=200)
    create_date = models.DateTimeField('date createded')
    def __str__(self):
        return self.type_text
    def was_created_recently(self):
        #return self.create_date >= timezone.now() - datetime.timedelta(days=3)
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.create_date <= now

class Algorithm(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    algorithm_text = models.CharField(max_length=200)
    times = models.IntegerField(default=0)
    result = models.CharField(max_length=5000)
    def __str__(self):
        return self.algorithm_text
