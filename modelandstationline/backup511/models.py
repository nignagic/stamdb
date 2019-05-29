from django.db import models

class Prefecture(models.Model):
	pref_cd = models.IntegerField(default=0)
	pref_name = models.CharField(max_length=200)
	def __str__(self):
		return self.pref_name

class Line(models.Model):
	line_cd = models.IntegerField(default=0, unique=True)
	company_cd = models.IntegerField(default=0)
	line_name = models.CharField(max_length=200)
	line_name_k = models.CharField(max_length=200, null=True, blank=True)
	line_name_h = models.CharField(max_length=200, null=True, blank=True)
	line_color_c = models.CharField(max_length=200, null=True, blank=True)
	line_color_t = models.CharField(max_length=200, null=True, blank=True)
	line_type = models.CharField(max_length=200, null=True, blank=True)
	lon = models.CharField(max_length=200, null=True, blank=True)
	lat = models.CharField(max_length=200, null=True, blank=True)
	zoom = models.IntegerField(default=0)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	pref_cds = models.ManyToManyField(Prefecture, blank=True)
	def __str__(self):
		return self.line_name

class Station(models.Model):
	station_cd = models.IntegerField(default=0, unique=True)
	station_g_cd = models.IntegerField(default=0)
	station_name = models.CharField(max_length=200)
	station_name_k = models.CharField(max_length=200, null=True, blank=True)
	station_name_r = models.CharField(max_length=200, null=True, blank=True)
	line_cd = models.ForeignKey(Line, to_field='line_cd', on_delete=models.CASCADE)
	pref_cd = models.IntegerField(default=0)
	post = models.CharField(max_length=200)
	add = models.CharField(max_length=200)
	lon = models.CharField(max_length=200)
	lat = models.CharField(max_length=200)
	open_ymd = models.CharField(max_length=200, null=True, blank=True)
	close_ymd = models.CharField(max_length=200, null=True, blank=True)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	def __str__(self):
		return self.station_name

class NonListStation(models.Model):
	station_g_cd = models.IntegerField(default=0)
	station_name = models.CharField(max_length=200)
	station_name_k = models.CharField(max_length=200, null=True, blank=True)
	station_name_r = models.CharField(max_length=200, null=True, blank=True)
	line_cd = models.ForeignKey(Line, to_field='line_cd', on_delete=models.CASCADE)
	pref_cd = models.IntegerField(default=0)
	post = models.CharField(max_length=200, null=True, blank=True)
	add = models.CharField(max_length=200)
	lon = models.CharField(max_length=200)
	lat = models.CharField(max_length=200)
	open_ymd = models.CharField(max_length=200, null=True, blank=True)
	close_ymd = models.CharField(max_length=200, null=True, blank=True)
	e_status = models.IntegerField(default=0)
	e_sort = models.IntegerField(default=0)
	def __str__(self):
		return self.station_name

class Category(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Creator(models.Model):
	name = models.CharField(max_length=200)
	channelId = models.CharField(max_length=200, primary_key=True)
	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField('title', max_length=255, blank=True, null=True)
	def __str__(self):
		return self.title

class Artist(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Song(models.Model):
	name = models.CharField(max_length=200)
	artist = models.ManyToManyField(Artist)
	def __str__(self):
		return self.name

class Vocal(models.Model):
	name = models.CharField(max_length=200)
	def __str__(self):
		return self.name

class Movie(models.Model):
	title = models.CharField('動画タイトル', max_length=200)
	channel = models.ForeignKey(
		Creator, on_delete=models.SET_NULL, null=True, verbose_name='投稿チャンネル'
	)
	main_id = models.CharField('動画ID', max_length=200, unique=True)
	youtube_id = models.CharField('YouTubeのID', max_length=200, blank=True)
	niconico_id = models.CharField('ニコニコ動画のID', max_length=200, blank=True)
	published_at = models.DateTimeField('投稿日時', blank=True, null=True)
	duration = models.DurationField('動画の長さ', null=True);
	n_view = models.IntegerField('再生回数', default=0, blank=True)
	n_like = models.IntegerField('高評価数', default=0, blank=True)
	n_dislike = models.IntegerField('低評価数', default=0, blank=True)
	n_comment = models.IntegerField('コメント数', default=0, blank=True)
	description = models.TextField('説明', blank=True)

	reg_date = models.DateTimeField('データベース登録日時', blank=True)

	song = models.ManyToManyField(Song, blank=True, verbose_name='使用楽曲')
	artist = models.ManyToManyField(Artist, blank=True, verbose_name='アーティスト')
	vocal = models.ManyToManyField(Vocal, blank=True, verbose_name='使用ボーカル')

	COLLAB = (
		('S', '単作'),
		('C', '合作')
	)
	is_collab = models.CharField('合作か', max_length=1, choices=COLLAB, default='S')
	def __str__(self):
		return self.title

class StationInMovie(models.Model):
	id_in_movie = models.IntegerField()
	station_cd = models.ForeignKey(Station, to_field='station_cd', on_delete=models.CASCADE)
	station_name = models.CharField(max_length=200)
	movie = models.ForeignKey(Movie, to_field='main_id', on_delete=models.CASCADE)
	non_line = models.BooleanField('路線不定', default=False)
	back_rel = models.IntegerField('back station relationship', default=0)
	creator_m = models.ManyToManyField(Creator, related_name="movie_creator", blank=True)
	creator_a = models.ManyToManyField(Creator, related_name="audio_creator", blank=True)
	reg_date = models.DateTimeField('更新日時', blank=True, null=True)
	def __str__(self):
		return self.station_name