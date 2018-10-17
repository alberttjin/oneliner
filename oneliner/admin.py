from django.contrib import admin
from . models import Event, Task, Profile

# Register your models here.
admin.site.register(Event)
admin.site.register(Task)
admin.site.register(Profile)