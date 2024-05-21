from rest_framework import viewsets, generics
from .serializers import *
from .models import *


class PerevalViewset(viewsets.ModelViewSet):
    queryset = Pereval.objects.all()
    serializer_class = PerevalSerializer


class TouristViewset(viewsets.ModelViewSet):
    queryset = Tourist.objects.all()
    serializer_class = TouristSerializer


class CoordinatesViewset(viewsets.ModelViewSet):
    queryset = Coordinates.objects.all()
    serializer_class = CoordinatesSerializer


class LevelViewset(viewsets.ModelViewSet):
    queryset = Level.objects.all()
    serializer_class = LevelSerializer


class PerevalImageViewset(viewsets.ModelViewSet):
    queryset = PerevalImage.objects.all()
    serializer_class = PerevalImageSerializer


class PerevalAddedViewset(generics.ListCreateAPIView):
    queryset = Pereval.objects.all()
    serializer_class = PerevalAddedSerializer


