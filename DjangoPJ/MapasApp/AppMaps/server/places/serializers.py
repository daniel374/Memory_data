from django.contrib.auth.models import User, Group
from .models import Localidades
from rest_framework import serializers

class LocalidadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Localidades
        fields = ['cod_localidad', 'local_nombre']

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']