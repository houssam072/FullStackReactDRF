from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    def create(self, validated_data):
        user = User.objects.create_user(
            username= validated_data['username'],
            email= validated_data['email'],
            password= validated_data['password']
        )
        return user
    
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'password')

    # def validate(self, data):
    #     user =  authenticate(username = data['username'], password = data['password'])
    #     if user and user.is_active:
    #         return user
    #     raise serializers.ValidationError('Incorrect Credentials')