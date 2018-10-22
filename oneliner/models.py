from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_auth_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)


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
    date = models.DateField()
    repeat_inf = models.BooleanField(default=False)
    repeat_times = models.IntegerField()
    repeat_freq = models.IntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    events = models.ManyToManyField(Event)
    tasks = models.ManyToManyField(Task)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
