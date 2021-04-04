import json
from django.contrib.auth import authenticate
from users.models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class LoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        print(self.__dict__)
        try:
            request = self._kwargs['data']
        except KeyError:
            pass

        request_data = request
        if ("username" in request_data and "password" in request_data):
            username = request_data['username']
            password = request_data['password']
            user = User.objects.filter(username=username)
            if user:
                user = authenticate(username=username, password=password)
                if user:
                    if not user.is_superuser and not user.is_staff:
                        raise serializers.ValidationError(
                            detail={
                                'message':
                                    'Usuario no autorizado a iniciar sesión'
                            },
                            code=403)
                else:
                    raise serializers.ValidationError(
                        detail={
                            'message': 'Usuario o Contraseña Incorrectos'
                        }, code=400)
            else:
                raise serializers.ValidationError(
                    detail={
                        'message': 'Usuario o Contraseña Incorrectos'
                    }, code=404)
            return super().validate(attrs)
        else:
            raise serializers.ValidationError(
                detail={
                    'message': 'Usuario y Contrasela son requeridos'
                }, code=400)

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['estado'] = user.estado.id
        return token