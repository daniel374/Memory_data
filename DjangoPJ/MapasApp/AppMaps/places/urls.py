from django.contrib.auth.models import User
from django.conf.urls import url, include
from django.urls import path
from . import views
from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path(r'', views.LocalidadesListView.as_view()),
     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]