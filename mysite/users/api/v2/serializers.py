from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers


class LoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')
        user = User.objects.filter(email=email)
        if user:
            user = authenticate(username=user[0].username, password=password)
            if user:
                self.user = user
            else:
                raise serializers.ValidationError(
                    detail={'message': 'Correo o Contraseña Incorrectos'},
                    code=400)
        else:
            raise serializers.ValidationError(
                detail={'message': 'Correo o Contraseña Incorrectos'},
                code=404)
        return attrs