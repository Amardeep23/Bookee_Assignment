from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gymapp.views import GymViewSet

router = DefaultRouter()

router.register(r'gyms', GymViewSet, basename='gym')

urlpatterns = [
    path('', include(router.urls)),
]