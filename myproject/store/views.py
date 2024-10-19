from django.shortcuts import render
from rest_framework import generics
from .models import Items
from .serializers import ItemsSerializer


# Create your views here.

class ItemsAPIView(generics.ListAPIView):
    queryset = Items.objects.all()
    serializer_class = ItemsSerializer
