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
    
    class Meta:
        model = bikelanetbl
        fields = [
            'Bikelane_id',
            'Typeofwork',
            'Region',
            'BikeArea',
            'RoadSection',
            'BikeClass',
            'FundSource',
            'Bikelane_Code',
            'Length',
            'StartPointX',
            'StartPointY',
            'EndPointX',
            'EndPointY',
            'BikeDate',
            'Remarks',
            'Province',
            'status',
        ]
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['Typeofwork'] = instance.Typeofwork.Typeofwork
        representation['Region'] = instance.Region.Region
        representation['BikeArea'] = instance.BikeArea.BikeArea
        representation['RoadSection'] = instance.RoadSection.RoadSection
        representation['BikeClass'] = instance.BikeClass.BikeClass
        representation['FundSource'] = instance.FundSource.FundSource
        return representation
