from django.contrib.auth import authenticate
from rest_framework import serializers

from .models import MyUser
from .utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=6, write_only=True)
    password_confirmation = serializers.CharField(min_length=6, write_only=True)

    class Meta:
        model = MyUser
        fields = ('email', 'password', 'password_confirmation')

    def validate(self, validated_data):
        password = validated_data.get('password')
        password_confirmation = validated_data.get('password_confirmation')
        if password != password_confirmation:
            raise serializers.ValidationError('Passwords do not match')
        return validated_data

    def create(self, validated_data):
        """Этот метод вызывается когда сохраняется объект (self.save())"""
        email = validated_data.get('email')
        password = validated_data.get('password')
        user = MyUser.objects.create_user(email=email, password=password)
        send_activation_code(email=user.email, activation_code=user.activation_code)
        return user


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(
        label='Password',
        style={'input-type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)
            if not user:
                message = 'Unable to log in with provided credentials'
                raise serializers.ValidationError(message, code='authorization')

        else:
            message = 'Must include "email" and "password".'
            raise serializers.ValidationError(message, code='authorization')

        attrs['user'] = user
        return attrs
