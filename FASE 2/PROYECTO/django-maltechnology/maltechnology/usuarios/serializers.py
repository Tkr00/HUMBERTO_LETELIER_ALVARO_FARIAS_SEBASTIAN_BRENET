from rest_framework import serializers
from .models import Usuario, InfoHorno, InfoProduccion

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'rut', 'role']

class InfoHornoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoHorno
        fields = '__all__'

class InfoProduccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfoProduccion
        fields = '__all__'
