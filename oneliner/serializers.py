from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = User
#         fields = ('id', 'first_name', 'last_name', 'email',)

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
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    # def update(self, instance, validated_data):
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.username = validated_data.get('username', instance.username)
    #     instance.save()
    #     return instance

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')