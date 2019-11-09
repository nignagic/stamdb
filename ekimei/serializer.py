from rest_framework import serializers

from .models import Station, Line

class StationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Station
		fields = ('station_name', 'station_cd', 'line_cd')

class LineSerializer(serializers.ModelSerializer):
	class Meta:
		model = Line
		fields = ('line_name', 'line_cd')