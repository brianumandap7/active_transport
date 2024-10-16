from rest_framework import serializers
from .models import bikelanetbl, Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource

class TypeofworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeofwork
        fields = ['Typeofwork']

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['Region']

class BikeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeArea
        fields = ['BikeArea']

class RoadSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSection
        fields = ['RoadSection']

class BikeClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeClass
        fields = ['BikeClass']

class FundSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundSource
        fields = ['FundSource']

class BikelaneTblSerializer(serializers.ModelSerializer):
    Typeofwork = TypeofworkSerializer()
    Region = RegionSerializer()
    BikeArea = BikeAreaSerializer()
    RoadSection = RoadSectionSerializer()
    BikeClass = BikeClassSerializer()
    FundSource = FundSourceSerializer()

    class Meta:
        model = bikelanetbl
        fields = '__all__'
