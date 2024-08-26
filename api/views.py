from django.db import transaction
from rest_framework import status, viewsets

from rest_framework.response import Response

from api.models import User, Address
from api.serializers import UserSerializer, AddressSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
