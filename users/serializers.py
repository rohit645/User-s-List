from rest_framework import serializers
from users.models import Users, Geo, Company, Address

class GeoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geo
        fields = ('lat', 'lng')

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'catchPhrase', 'bs')

class AddressSerializer(serializers.ModelSerializer):
    geo = GeoSerializer(read_only=True, many=True)
    class Meta:
        model = Address
        fields = ('street', 'suite', 'city', 'zipcode', 'geo')

class UsersSerializer(serializers.ModelSerializer):
    address = AddressSerializer(read_only=True, many=True)
    company = CompanySerializer(read_only=True, many=True)
    class Meta:
        model = Users
        fields = '__all__'
