from django.urls import path, include
from app.views import *

urlpatterns = [
    path('car/create/', CarCreateView.as_view()),
    path('car/all/', CarsListView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
]