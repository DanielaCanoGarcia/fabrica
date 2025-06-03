from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Usuario
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
            if 'password' in validated_data:
                instance.set_password(validated_data.pop('password'))
            return super().update(instance, validated_data)

class UsuarioSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Usuario
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        usuario = Usuario.objects.create(user=user, **validated_data)
        return usuario
    
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', None)

        # Actualizar datos de Usuario (modelo actual)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        # Actualizar datos de User (si los hay)
        if user_data:
            user_instance = instance.user
            for attr, value in user_data.items():
                if attr == 'password':
                    user_instance.set_password(value)
                else:
                    setattr(user_instance, attr, value)
            user_instance.save()

        instance.save()
        return instance

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Agrega campos básicos del usuario
        token['username'] = user.username
        token['email'] = user.email
        token['is_staff'] = user.is_staff
        token['is_superuser'] = user.is_superuser

        # Agrega campos del modelo Usuario si existen
        if hasattr(user, 'usuario'):
            token['nombre'] = user.usuario.nombre
            token['apellido_pat'] = user.usuario.apellido_pat
            token['apellido_mat'] = user.usuario.apellido_mat
            token['area'] = user.usuario.area
            token['puesto'] = user.usuario.puesto

        return token
