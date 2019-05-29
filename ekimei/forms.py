from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import Movie, Station, NonListStation, Line, StationInMovie, Post


# class MovieForm(ModelForm):
# 	formset_class = StationInMovieFormSet
# 	class Meta:
# 		model = Movie
# 		fields = ('title',)

class MovieRegisterForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_dislike', 'n_comment', 'description', 'reg_date', 'song', 'vocal', 'is_collab')
		widgets = {
			'title': forms.HiddenInput(attrs={
				'class': 'title',
			}),
			'channel': forms.HiddenInput(attrs={
				'id': 'channel',
			}),
			'main_id': forms.HiddenInput(attrs={
				'class': 'main_id',
			}),
			'youtube_id': forms.HiddenInput(attrs={
				'class': 'youtube_id',
			}),
			'niconico_id': forms.HiddenInput(attrs={
				'class': 'niconico_id',
			}),
			'published_at': forms.HiddenInput(attrs={
				'class': 'published_at',
			}),
			'duration': forms.HiddenInput(attrs={
				'class': 'duration',
			}),
			'n_view': forms.HiddenInput(attrs={
				'class': 'n_view',
			}),
			'n_like': forms.HiddenInput(attrs={
				'class': 'n_like',
			}),
			'n_dislike': forms.HiddenInput(attrs={
				'class': 'n_dislike',
			}),
			'n_comment': forms.HiddenInput(attrs={
				'class': 'n_comment',
			}),
			'description': forms.HiddenInput(attrs={
				'class': 'description',
			}),
			'reg_date': forms.HiddenInput(attrs={
				'class': 'reg_date',
			}),
		}
class MovieUpdateForm(forms.ModelForm):
	class Meta:
		model = Movie
		fields = ('title', 'channel', 'main_id', 'youtube_id', 'niconico_id', 'published_at', 'duration', 'n_view', 'n_like', 'n_dislike', 'n_dislike', 'n_comment', 'description', 'reg_date', 'song', 'vocal', 'is_collab')
		widgets = {
			'title': forms.HiddenInput(attrs={
				'class': 'title',
			}),
			'channel': forms.HiddenInput(attrs={
				'id': 'channel',
			}),
			'main_id': forms.HiddenInput(attrs={
				'class': 'main_id',
			}),
			'youtube_id': forms.HiddenInput(attrs={
				'class': 'youtube_id',
			}),
			'niconico_id': forms.HiddenInput(attrs={
				'class': 'niconico_id',
			}),
			'published_at': forms.HiddenInput(attrs={
				'class': 'published_at',
			}),
			'duration': forms.HiddenInput(attrs={
				'class': 'duration',
			}),
			'n_view': forms.HiddenInput(attrs={
				'class': 'n_view',
			}),
			'n_like': forms.HiddenInput(attrs={
				'class': 'n_like',
			}),
			'n_dislike': forms.HiddenInput(attrs={
				'class': 'n_dislike',
			}),
			'n_comment': forms.HiddenInput(attrs={
				'class': 'n_comment',
			}),
			'description': forms.HiddenInput(attrs={
				'class': 'description',
			}),
			'reg_date': forms.HiddenInput(attrs={
				'class': 'reg_date',
			}),
			'song': forms.SelectMultiple(attrs={
				'class': 'song',
			}),
			'vocal': forms.SelectMultiple(attrs={
				'class': 'vocal',
			}),
			'is_collab': forms.Select(attrs={
				'class': 'is_collab',
			}),
		}

class StationInMovieForm(forms.ModelForm):
	BACKREL_CHOICES = [
		(0, '同一駅'),
		(1, 'つながっている'),
		(2, '離れている'),
	]
	id_in_movie = forms.IntegerField(
		label='順番', widget=forms.HiddenInput
	)
	back_rel = forms.ChoiceField(
		label='前駅関係', choices=BACKREL_CHOICES, widget=forms.Select
	)
	station_name = forms.CharField(
		label='歌唱名', max_length=50
	)
	station_nonlist_cd = forms.ModelChoiceField(
		NonListStation.objects, widget=forms.HiddenInput
	)
	class Meta:
		model = StationInMovie
		fields = ('id', 'id_in_movie', 'station_cd', 'station_nonlist_cd', 'station_name', 'movie', 'non_line', 'back_rel', 'creator_m', 'creator_a', 'reg_date')
		widgets = {
			'id': forms.HiddenInput(),
			'id_in_movie': forms.TextInput(attrs={
				'class': 'id_in_movie',
			}),
			'station_cd': forms.HiddenInput(attrs={
				'class': 'station_cd',
			}),
			'station_nonlist_cd': forms.HiddenInput(attrs={
				'class': 'station_nonlist_cd',
			}),
			'station_name': forms.TextInput(attrs={
				'class': 'station_name',
			}),
			'movie': forms.Select(attrs={
				'class': 'movie',
			}),
			'non_line': forms.CheckboxInput(attrs={
				'class': 'non_line',
			}),
			'back_rel': forms.TextInput(attrs={
				'class': 'back_rel',
			}),
			'creator_m': forms.CheckboxSelectMultiple(attrs={
				'class': 'creator_m',
			}),
			'creator_a': forms.CheckboxSelectMultiple(attrs={
				'class': 'creator_a',
			}),
			'reg_date': forms.HiddenInput(attrs={
				'class': 'reg_date',
			}),
		}

	# def __init__(self, *args, **kwargs):
	# 	super().__init__(*args, **kwargs)
	# 	for field in self.fields.values():
	# 		field.widget.attrs['class'] = 'form-control'

StationInMovieFormset = forms.inlineformset_factory(
	parent_model = Movie,
	model = StationInMovie,
	form = StationInMovieForm,
	extra = 0,
	can_delete = False
)

class MovieRegisterPrototypeForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = '__all__'
		widgets = {
			'title': forms.HiddenInput(attrs={
				'class': 'title_name',
			}),
		}

class StationCreateForm(forms.ModelForm):
	class Meta:
		model = Station
		fields = '__all__'

class StationCreatebyLineForm(forms.ModelForm):
	class Meta:
		model = Station
		fields = '__all__'
		widgets = {
			'station_cd': forms.HiddenInput(attrs={
				'class': 'station_cd',
			}),
			'station_g_cd': forms.HiddenInput(attrs={
				'class': 'station_g_cd',
			}),
			'line_cd': forms.HiddenInput(attrs={
				'class': 'line_cd',
			}),
			'e_status': forms.RadioSelect(attrs={
				'class': 'e_status',
			}),
			'e_sort': forms.HiddenInput(attrs={
				'class': 'e_sort',
			}),
		}

class LineCreateForm(forms.ModelForm):
	class Meta:
		model = Line
		fields = '__all__'
		widgets = {
			'line_cd': forms.TextInput(attrs={
				'class': 'line_cd',
			}),
		}