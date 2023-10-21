from rest_framework import viewsets
from rest_framework.response import Response
from .models import Gym, Trainer, Client, WorkoutSession
from .serializers import GymSerializer, TrainerSerializer, ClientSerializer, WorkoutSessionSerializer


class GymViewSet(viewsets.ModelViewSet):
    queryset = Gym.objects.all()
    serializer_class = GymSerializer

