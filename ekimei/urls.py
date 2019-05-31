from django.urls import path
from . import views

app_name = 'ekimei'

urlpatterns = [
	path('list/', views.MovieListView.as_view(), name="list"),
	path('movie/<slug:main_id>/', views.MovieDetailView.as_view(), name='detail'),
	path('list/creator/', views.MovieListbyCreatorView.as_view(), name='creator_list'),
	path('line/<int:line_cd>/', views.MovieListbyLineView.as_view(), name='line_list'),
	path('station/<int:station_cd>/', views.MovieListbyStationView.as_view(), name='station_list'),
	# path('song/<int:id>/', views.MovieListbySongView.as_view(), name='song_list'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('registerprototype/', views.MovieRegisterPrototypeView.as_view(), name='registerprototype'),
	path('station_create/', views.StationCreate.as_view(), name='station_create'),
	path('station_create/<int:line_cd>/', views.StationCreatebyLine.as_view(), name='station_create_line'),
	path('line_create/', views.LineCreate.as_view(), name='line_create'),
	path('popup/song_create/', views.PopupSongCreate.as_view(), name='popup_song_create'),
	path('popup/artist_create/', views.PopupArtistCreate.as_view(), name='popup_artist_create'),
	path('popup/vocal_create/', views.PopupVocalCreate.as_view(), name='popup_vocal_create'),
	path('edit/<slug:main_id>/', views.update_movie, name='edit'),
	path('upload/', views.upload, name='upload'),
	path('uploadline/', views.uploadline, name='uploadline'),
	path('uploadpref/', views.uploadpref, name='uploadpref'),
	path('lineprefset/', views.lineprefset, name='lineprefset'),
]