from django.db import models

# Create your models here.
class User(models.Model):
    joined = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=100, blank=True, default='')
    last_name = models.CharField(max_length=100, blank=True, default='')
    email = models.CharField(max_length=100, blank=False)
    # TODO: add password
    # events = models.ManyToManyField(Event)
    # tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.email