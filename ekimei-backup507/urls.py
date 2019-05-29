from django.urls import path
from . import views

app_name = 'ekimei'

urlpatterns = [
	path('list', views.MovieListView.as_view(), name="list"),
	path('movie/<slug:youtube_id>/', views.MovieDetailView.as_view(), name='detail'),
	path('register/', views.MovieRegisterView.as_view(), name='register'),
	path('upload/', views.upload, name='upload'),
	path('uploadline/', views.uploadline, name='uploadline'),
]