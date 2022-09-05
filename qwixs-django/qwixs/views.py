from django.shortcuts import render
from rest_framework import generics
from .models import Owner, Business, Services
from .serializers import OwnerSerializer, BusinessSerializer, ServicesSerializer


# Create your views here.

class BusinessList(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class BusinessDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer


class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class ServicesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
