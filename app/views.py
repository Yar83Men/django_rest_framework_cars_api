from rest_framework import generics
from app.models import Car
from app.serializers import CarDetailSerializer, CarListSerializer
from app.permissions import IsOwnerOrReadOnly
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication

class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarsListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    permission_classes = (IsAuthenticated, )


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarDetailSerializer
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication, BasicAuthentication, SessionAuthentication)
    permission_classes = (IsOwnerOrReadOnly, IsAdminUser)

