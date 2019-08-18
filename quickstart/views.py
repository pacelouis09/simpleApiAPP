from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.generics import UpdateAPIView

from quickstart.serializers import UserSerializer, GroupSerializer, \
    CustomerSerializer, AccountSerializer, BackgroundSerializer
from .models import Customer, Account, Background
from rest_framework import generics
from rest_framework.viewsets import ViewSetMixin
from rest_framework import renderers
from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


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

# class CustomersList(APIView):
#     """
#     List all Customers, or create a new customer
#     """
#     def get(self, request, format=None):
#         customers = Customers.objects.all()
#         serializer = CustomerSerializer(customers, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HHTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(ViewSetMixin, generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Customer(ViewSetMixin, generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class Account(ViewSetMixin, generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class Background(ViewSetMixin, generics.ListCreateAPIView):
    queryset = Background.objects.all()
    serializer_class = BackgroundSerializer


# class BackgroundUpdateDetail(UpdateAPIView):
#     queryset = Background.objects.all()
#     serializer_class = BackgroundSerializer
