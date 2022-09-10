from rest_framework import serializers
from .models import Owner, Business, Services


class OwnerSerializer(serializers.ModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='owner_detail',
        many=False,
        read_only=True
    )

    class Meta:
        model = Owner
        fields = ('id', 'first_name', 'last_name', 'email',
                  'username', 'password', 'business')


class BusinessSerializer(serializers.ModelSerializer):
    services = serializers.HyperlinkedRelatedField(
        view_name='services_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = Business
        fields = ('id', 'name', 'about', 'address', 'city', 'state',
                  'zipcode', 'phone', 'email', 'owner', 'services')


class ServicesSerializer(serializers.ModelSerializer):
    business = serializers.HyperlinkedRelatedField(
        view_name='business_detail',
        read_only=True
    )

    class Meta:
        model = Services
        fields = ('id', 'name', 'description', 'business')
