from django.db import models

class Line(models.Model):
	line_cd = models.IntegerField(default=0)
	company_cd = models.IntegerField(default=0)
	line_name = models.CharField(max_length=200)
	line_name_k = models.CharField(max_length=200)
	line_name_h = models.CharField(max_length=200)
	line_color_c = models.CharField(max_length=200)
	line_color_t = models.CharField(max_length=200)
	line_type = models.CharField(max_length=200)
	lon = models.CharField(max_length=200)
	lat = models.CharField(max_length=200)
	zoom = models.IntegerField(default=0)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	def __str__(self):
		return self.line_name

class Station(models.Model):
	station_cd = models.IntegerField(default=0)
	station_g_cd = models.IntegerField(default=0)
	station_name = models.CharField(max_length=200)
	station_name_k = models.CharField(max_length=200)
	station_name_r = models.CharField(max_length=200)
	line_cd = models.IntegerField(default=0)
	pref_cd = models.IntegerField(default=0)
	post = models.CharField(max_length=200)
	add = models.CharField(max_length=200)
	lon = models.CharField(max_length=200)
	lat = models.CharField(max_length=200)
	open_ymd = models.CharField(max_length=200)
	close_ymd = models.CharField(max_length=200)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	def __str__(self):
		return self.station_name

class Movie(models.Model):
	title = models.CharField(max_length=200)
	reg_date = models.DateTimeField('date registered')
	youtube_id = models.CharField(max_length=200, null=True)
	niconico_id = models.CharField(max_length=200, null=True)
	# line = models.ManyToManyField(Line)
	def __str__(self):
		return self.title

class Creator(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class StationInMovie(models.Model):
	id_in_movie = models.IntegerField()
	station_cd = models.ForeignKey(Station, on_delete=models.SET_NULL, null=True)
	station_name = models.CharField(max_length=200)
	movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
	line_cd = models.ForeignKey(Line, on_delete=models.SET_NULL, null=True)
	back_rel = models.IntegerField('back station relationship', default=0)
	creator_m = models.ManyToManyField(Creator, related_name="movie_creator")
	creator_a = models.ManyToManyField(Creator, related_name="audio_creator")
	def __str__(self):
		return self.station_name
