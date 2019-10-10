error_404_viewfrom django.shortcuts import render
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
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS #, token
from rest_framework_api_key.permissions import HasAPIKey


# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status


def error_404_view(request, exception):
    data = {"name": "PayPaI.com"}
    return render(request, "temmplates/404.html")

# Create your views here.

class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = [HasAPIKey | IsAuthenticated]
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

#     def post(self, request, format=None):
#         serializer = CustomerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HHTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(generics.ListAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(ViewSetMixin, generics.RetrieveAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Customer(ViewSetMixin, generics.ListCreateAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Customer.objects.all().order_by('id')
    serializer_class = CustomerSerializer


class Account(ViewSetMixin, generics.ListCreateAPIView):
    # authentication_classes = (TokenAuthentication, )
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, format=None):
        content = {
            'status': 'request was permitted'
        }
        return Response(content)


class Background(ViewSetMixin, generics.ListCreateAPIView):
    permission_classes = [HasAPIKey | IsAuthenticated]
    queryset = Background.objects.all().order_by('-id')
    serializer_class = BackgroundSerializer
