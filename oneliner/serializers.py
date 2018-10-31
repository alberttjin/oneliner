from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from .models import Task, Profile

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField()

    def create(self, validated_data):
        user = User.objects.create_user (
                validated_data['username'],
                validated_data['email'],
                validated_data['password']
            )
        return user

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    date = serializers.DateField(required=True)
    repeat_inf = serializers.IntegerField()
    repeat_times = serializers.IntegerField()
    repeat_freq = serializers.IntegerField()

    def create(self, validated_data):
        task = Task.objects.create (
                name=validated_data['name'],
                date=validated_data['date'],
                repeat_inf=validated_data['repeat_inf'],
                repeat_times=validated_data['repeat_times'],
                repeat_freq=validated_data['repeat_freq'],
            )
        profile = self.context['profile']
        profile.tasks.add(task)
        profile.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.date = validated_data.get('date', instance.date)
        instance.repeat_inf = validated_data.get('repeat_inf', instance.repeat_inf)
        instance.repeat_times = validated_data.get('repeat_times', instance.repeat_times)
        instance.repeat_freq = validated_data.get('repeat_freq', instance.repeat_freq)
        instance.save()
        return instance

    class Meta:
        model = Task
        fields = ('id', 'name', 'date', 'repeat_inf', 'repeat_times', 'repeat_freq')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    tasks = TaskSerializer(many=True)

    class Meta:
        model = Profile
        fields = ('user', 'tasks')
    
