from django.shortcuts import render
from django.contrib.auth.models import User, Group
from .models import Food, Ingredient, LogEntry
from rest_framework import viewsets
from .serializers import UserSerializer, GroupSerializer, FoodSerializer, LogEntrySerializer
# Create your views here.

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


class FoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

class LogEntryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = LogEntry.objects.all()
    serializer_class = LogEntrySerializer

