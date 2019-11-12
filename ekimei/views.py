import django_filters
from rest_framework import viewsets, filters, generics
from . import serializer
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.forms import ModelForm, inlineformset_factory

from . import forms

from .models import Prefecture, Line, Station, Movie, StationInMovie, Post, Song, Artist, Vocal
import csv
from io import TextIOWrapper

# class MovieListView(generic.ListView):
# 	template_name = 'ekimei/list.html'
# 	context_object_name = 'latest_movie_list'

# 	def get_queryset(self):
		# return Movie.objects.order_by('-reg_date')

class MovieListView(generic.ListView):
	template_name = 'ekimei/listbycreator.html'
	context_object_name = 'latest_movie_list'

	def get_queryset(self):
		return Movie.objects.order_by('-published_at').order_by('-channel')

class MovieListbyStationView(generic.ListView):
	template_name = 'ekimei/moviebystationlist.html'
	context_object_name = "station_matches"

	def get_queryset(self, **kwargs):
		station = Station.objects.get(station_cd=self.kwargs['station_cd'])
		return Station.objects.filter(station_g_cd=station.station_g_cd)

class MovieListbyLineView(generic.ListView):
	model = Line
	template_name = 'ekimei/moviebylinelist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		stations = Station.objects.filter(line_cd=self.kwargs['line_cd'])
		movies = []
		for station in stations:
			stationinmovieall = StationInMovie.objects.filter(station_cd=station)
			for stationinmovie in stationinmovieall:
				movies.append(stationinmovie.movie)
		movies_unique_order = sorted(set(movies), key=movies.index)

		line = Line.objects.get(line_cd=self.kwargs['line_cd'])
		context = {
			'line': line,
			'movies': movies_unique_order
		}
		return context

class MovieListbySongView(generic.ListView):
	model = Song
	template_name = 'ekimei/moviebysonglist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		movies = Movie.objects.filter(song=self.kwargs['id']).order_by('-published_at')

		song = Song.objects.get(pk=self.kwargs['id'])
		context = {
			'song': song,
			'movies': movies
		}
		return context

class MovieListbyVocalView(generic.ListView):
	model = Vocal
	template_name = 'ekimei/moviebyvocallist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		movies = Movie.objects.filter(vocal=self.kwargs['id']).order_by('-published_at')

		vocal = Vocal.objects.get(pk=self.kwargs['id'])
		context = {
			'vocal': vocal,
			'movies': movies
		}
		return context

class MovieDetailView(generic.DetailView):
	model = Movie
	slug_field = "main_id"
	slug_url_kwarg = "main_id"
	template_name = 'ekimei/detail.html'

class MovieRegisterView(generic.CreateView):
	template_name = 'ekimei/register.html'
	model = Movie
	form_class = forms.MovieRegisterForm
	def get_success_url(self):
		return reverse_lazy('ekimei:edit', kwargs={'main_id': self.object.main_id})

class StationCreate(generic.CreateView):
	template_name = 'ekimei/station_form.html'
	model = Station
	form_class = forms.StationCreateForm
	success_url = reverse_lazy('ekimei:station_create')

class StationCreatebyLine(generic.CreateView):
	template_name = 'ekimei/station_form_line.html'
	model = Station
	form_class = forms.StationCreatebyLineForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		form = forms.StationCreatebyLineForm
		line = Line.objects.get(line_cd=self.kwargs['line_cd'])
		stations = Station.objects.filter(line_cd=line)
		station_cds = []
		for station in stations:
			station_cds.append(station.station_cd)
		station_cd = max(station_cds) + 1
		context = {
			'form': form,
			'station_cd': station_cd,
			'line': line
		}
		return context

	def get_success_url(self):
		return reverse_lazy('ekimei:station_create_line', kwargs={'line_cd': self.kwargs['line_cd']})

class LineCreate(generic.CreateView):
	template_name = 'ekimei/line_form.html'
	model = Line
	form_class = forms.LineCreateForm

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		form = forms.LineCreateForm
		lines = Line.objects.all()
		line_cds = []
		for line in lines:
			line_cds.append(line.line_cd)
		line_cd = max(line_cds) + 1
		context = {
			'form': form,
			'line_cd': line_cd
		}
		return context

	def get_success_url(self):
		return reverse_lazy('ekimei:station_create_line', kwargs={'line_cd': self.kwargs['line_cd']})

class SongCreate(generic.CreateView):
	model = Song
	fields = '__all__';
	success_url = reverse_lazy('ekimei:list')

class PopupSongCreate(SongCreate):
	def form_valid(self, form):
		song = form.save()
		context = {
			'object_name': str(song),
			'object_pk': song.pk,
			'function_name': 'add_song'
		}

		return render(self.request, 'ekimei/close.html', context)

class ArtistCreate(generic.CreateView):
	model = Artist
	fields = '__all__';
	success_url = reverse_lazy('ekimei:list')

class PopupArtistCreate(ArtistCreate):
	def form_valid(self, form):
		artist = form.save()
		context = {
			'object_name': str(artist),
			'object_pk': artist.pk,
			'function_name': 'add_artist'
		}

		return render(self.request, 'ekimei/close.html', context)

class VocalCreate(generic.CreateView):
	model = Vocal
	fields = ('name',)
	success_url = reverse_lazy('ekimei:list')

class PopupVocalCreate(VocalCreate):
	def form_valid(self, form):
		vocal = form.save()
		context = {
			'object_name': str(vocal),
			'object_pk': vocal.pk,
			'function_name': 'add_vocal'
		}

		return render(self.request, 'ekimei/close.html', context)

def update_movie(request, main_id):
	movie = get_object_or_404(Movie, main_id=main_id)
	form = forms.MovieUpdateForm(request.POST or None, instance=movie)
	formset = forms.StationInMovieFormset(request.POST or None, instance=movie)
	# prefs = Prefecture.objects.all()
	# linebypref = []
	# for pref in prefs:
	# 	linebypref.append(Line.objects.filter(pref_cds=pref.pref_cd))
	# lines = Line.objects.all()
	# stations = Station.objects.all().order_by('-e_sort').order_by('line_cd')
	if request.method == 'POST' and form.is_valid() and formset.is_valid():
		allstation = StationInMovie.objects.filter(movie=movie)
		allstation.delete()
		form.save()
		formset.save()
		return redirect('ekimei:detail', main_id=main_id)

	context = {
		'movie': movie,
		'form': form,
		'formset': formset,
		# 'prefs': prefs,
		# 'linebypref': linebypref,
		# 'lines': lines,
		# 'stations': stations
	}

	# return render(request, 'ekimei/edit.html', context)
	return render(request, 'ekimei/editbyjson.html', context)

class MovieRegisterPrototypeView(generic.CreateView):
	template_name = 'ekimei/register-prototype.html'
	model = Post
	form_class = forms.MovieRegisterPrototypeForm
	success_url = reverse_lazy('ekimei:detail')

def upload(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			station, created = Station.objects.get_or_create(station_cd=line[0])
			station.station_cd = line[0]
			station.station_g_cd = line[1]
			station.station_name = line[2]
			station.station_name_k = line[3]
			station.station_name_r = line[4]
			station.line_cd = Line.objects.get(line_cd=line[5])
			station.pref_cd = Prefecture.objects.get(pref_cd=line[6])
			station.post = line[7]
			station.add = line[8]
			station.lon = line[9]
			station.lat = line[10]
			if line[11] != '':
				station.open_ymd = line[11]
			if line[12] != '':
				station.close_ymd = line[12]
			station.e_status = line[13]
			station.e_sort = line[14]
			station.save()

		return render(request, 'ekimei/upload.html')

	else:
		return render(request, 'ekimei/upload.html')

def uploadline(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			l, created = Line.objects.get_or_create(line_cd=line[0])
			l.line_cd = line[0]
			l.company_cd = line[1]
			l.line_name = line[2]
			l.line_name_k = line[3]
			l.line_name_h = line[4]
			l.line_color_c = line[5]
			l.line_color_t = line[6]
			l.line_type = line[7]
			l.lon = line[8]
			l.lat = line[9]
			l.zoom = line[10]
			l.e_status = line[11]
			l.e_sort = line[12]
			l.save()

		return render(request, 'ekimei/upload.html')

	else:
		return render(request, 'ekimei/upload.html')

def uploadpref(request):
	if 'csv' in request.FILES:
		form_data = TextIOWrapper(request.FILES['csv'].file, encoding='utf-8')
		csv_file = csv.reader(form_data)
		for line in csv_file:
			pref, created = Prefecture.objects.get_or_create(pref_cd=line[0])
			pref.pref_cd = line[0]
			pref.pref_name = line[1]
			pref.save()

		return render(request, 'ekimei/upload.html')

	else:
		return render(request, 'ekimei/upload.html')

def lineprefset(request):
	stations = Station.objects.all()
	for station in stations:
		line = station.line_cd
		pref = station.pref_cd
		line.pref_cds.add(pref)

	return render(request, 'ekimei/lineprefset.html')

class StationViewSet(generics.ListAPIView):
	serializer_class = serializer.StationSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['line_cd']
		return Station.objects.filter(line_cd=query_my_name)

class LineViewSet(generics.ListAPIView):
	serializer_class = serializer.LineSerializer
	def get_queryset(self):
		query_my_name = self.kwargs['pref_cd']
		return Line.objects.filter(pref_cds=query_my_name)