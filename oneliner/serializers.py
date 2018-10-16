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

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class TaskSerializer(serializers.ModelSerializer):
    name = serializers.CharField(required=True)
    day = serializers.DateField(required=True)
    repeat_inf = serializers.IntegerField()
    repeat_times = serializers.IntegerField()
    repeat_freq = serializers.IntegerField()

    def create(self, validated_data):
        task = Task.objects.create (
                name=validated_data['name'],
                day=validated_data['day'],
                repeat_inf=validated_data['repeat_inf'],
                repeat_times=validated_data['repeat_times'],
                repeat_freq=validated_data['repeat_freq'],
            )
        return task

    class Meta:
        model = Task
        fields = ('id', 'name', 'day', 'repeat_inf', 'repeat_times', 'repeat_freq')

class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    tasks = TaskSerializer(required=True, many=True)

    def create(self, validated_data):
        user = User.objects.create_user (
                validated_data['username'],
                validated_data['email'],
                validated_data['password']
            )
        profile = user.profile
        return profile

    class Meta:
        model = Profile
        fields = ('user', 'tasks')
    
    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.save()
    #     return instance
