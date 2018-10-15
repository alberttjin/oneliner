from django.db import models

# Create your models here.
class Event(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    start = models.DateTimeField()
    end = models.DateTimeField()
    repeat_inf = models.BooleanField(default=False)
    repeat_times = models.IntegerField()
    repeat_freq = models.IntegerField()

    def __str__(self):
        return self.name

class Task(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    day = models.DateField()
    repeat_inf = models.BooleanField(default=False)
    repeat_times = models.IntegerField()
    repeat_freq = models.IntegerField()

    def __str__(self):
        return self.name

