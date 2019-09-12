from django.urls import path, include
from rest_framework import routers

from account import views

router = routers.DefaultRouter()
router.register(r'profiles', views.ProfileViewSet)
urlpatterns = [
    path(r'', include(router.urls))
]
