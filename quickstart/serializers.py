from django.contrib.auth.models import User, Group
from .models import Customer, Account, Background
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # customers = serializers.PrimaryKeyRelatedField(many=True, queryset=Customers.objects.all())
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'password', 'groups') # 'customers'


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ('id', 'IP', 'location_by_ip', 'paid_status', 'name',
                  'email', 'phone', 'order_date', 'visit_date', 'guests_qty', 'guests_names')


class AccountSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Account
        # fields = ('id',  'phone', 'IP', 'username', 'password')
        fields = ('id', 'phone', 'username', 'password')


class BackgroundSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.CharField(source='get_absolute_url', read_only=True)

    class Meta:
        model = Background
        # fields = ('id', 'username','phone','password','confirmation_code',
        #           'street_address','address2', 'city','state','zip_code',
        #           'payment_numbers','expiration_month','expiration_year','cvv',
        #           'bank_name','IP',)
        fields = ('id', 'phone', 'street_address', 'address2', 'city', 'state', 'zip_code',
                  'payment_numbers', 'expiration', 'cvv')

