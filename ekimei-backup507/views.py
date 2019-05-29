from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.forms import ModelForm, inlineformset_factory

from .forms import MovieRegisterFormSet, StationInMovieForm

from extra_views import CreateWithInlinesView, InlineFormSet

from .models import Line, Station, Movie, StationInMovie
import csv
from io import TextIOWrapper

class ListView(generic.ListView):
	template_name = 'ekimei/list.html'
	context_object_name = 'latest_movie_list'

	def get_queryset(self):
		return Movie.objects.order_by('-reg_date')[:5]

class DetailView(generic.DetailView):
	model = Movie
	slug_field = "youtube_id"
	slug_url_kwarg = "youtube_id"
	template_name = 'ekimei/detail.html'

# class StationInlineFormSet(InlineFormSet):
# 	model = StationInMovie
# 	fields = ("id_in_movie", "station_cd", "back_rel", "creator_m", "creator_a")
# 	def get_context_data(self, **kwargs):
# 		context = super().get_context_data(**kwargs)
# 		default_data = {'back_rel': '1'}

# class MovieStationCreateFormsetView(CreateWithInlinesView):
# 	model = Movie
# 	form = MovieForm()
# 	fields = ("title", "youtube_id")
# 	inlines = [StationInlineFormSet, ]
# 	template_name = 'ekimei/edit.html'

# class EditView(generic.UpdateView):
# 	model = Movie
# 	form_class = MovieForm
# 	slug_field = "youtube_id"
# 	slug_url_kwarg = "youtube_id"
# 	template_name = 'ekimei/edit.html'
# 	success_url = reverse_lazy('ekimei:edit')

def add(request):
	formset = MovieRegisterFormSet(request.POST or None)
	if request.method == 'POST' and formset.is_valid():
		formset.save()
		return redirect('ekimei:detail')

	context = {
		'formset': formset
	}

	return render(request, 'ekimei/edit.html', context)

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
			station.line_cd = line[5]
			station.pref_cd = line[6]
			station.post = line[7]
			station.add = line[8]
			station.lon = line[9]
			station.lat = line[10]
			station.open_ymd = line[11]
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