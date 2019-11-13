from rest_framework import serializers
from rest_framework.serializers import SerializerMethodField

from .models import Station, Line

class StationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Station
		fields = ('station_name', 'station_cd', 'line_cd')

class LineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Line
		fields = ('line_name', 'line_cd')

class LineNameSerializer(serializers.ModelSerializer):
	class Meta:
		model = Line
		fields = ('line_name', 'line_cd')

class StationSearchSerializer(serializers.ModelSerializer):
	line_name = serializers.CharField(source='line_cd.line_name')
	class Meta:
		model = Station
		fields = ['station_name', 'station_cd', 'line_name']