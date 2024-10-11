from rest_framework import serializers
from .models import bikelanetbl, Typeofwork, Region, BikeArea, RoadSection, BikeClass, FundSource

class TypeofworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Typeofwork
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = '__all__'

class BikeAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeArea
        fields = '__all__'

class RoadSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoadSection
        fields = '__all__'

class BikeClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = BikeClass
        fields = '__all__'

class FundSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = FundSource
        fields = '__all__'

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
