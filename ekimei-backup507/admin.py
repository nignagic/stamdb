from django.contrib import admin

from .models import Line, Station, Movie, Creator, StationInMovie

class StationAdmin(admin.ModelAdmin):
	list_display = ('id', 'station_cd', 'station_name', 'line_cd', 'add')
	search_fields = ['station_name']

admin.site.register(Line)
admin.site.register(Station, StationAdmin)
admin.site.register(Movie)
admin.site.register(Creator)
admin.site.register(StationInMovie)