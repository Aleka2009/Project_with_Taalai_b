from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.core.exceptions import ValidationError


class RegisterSerializer(serializers.Serializer):
    login = serializers.CharField()
    password = serializers.CharField()

    def validate_login(self, value):
        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError('login already used')
        return value

    def validate_password(self, password):
        try:
            validate_password(password)
        except ValidationError as e:
            raise serializers.ValidationError(e)
        return password

    def create(self, validate_data):
        user = User.objects.create(username=validate_data.get('login'))
        user.set_password(validate_data.get('password'))
        user.save()
        return user
