from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Localidades

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import LocalidadSerializer, UserSerializer, GroupSerializer
# Create your views here.

from django.views import generic

class LocalidadesListView(generic.ListView):
    model = Localidades
    context_object_name = 'localidades_list'   # your own name for the list as a template variable
    queryset = Localidades.objects.all()[:5] # Get 5 books containing
    template_name = 'localidades.html'  # Specify your own template name/location


"""
Django -Rest Framework
"""
class LocalidadViewSet(viewsets.ModelViewSet):
    queryset = Localidades.objects.all().order_by('cod_localidad')
    serializer_class = LocalidadSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer