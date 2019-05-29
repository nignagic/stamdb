from django.forms import Form, ModelForm, inlineformset_factory
from django import forms
from .models import Movie, Station, StationInMovie


# class MovieForm(ModelForm):
# 	formset_class = StationInMovieFormSet
# 	class Meta:
# 		model = Movie
# 		fields = ('title',)

class MovieRegisterForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'

	class Meta:
		model = Movie
		fields = '__all__'

MovieRegisterFormSet = forms.modelformset_factory(
	Movie, form=MovieRegisterForm, extra=3
	)

class StationInMovieForm(forms.Form):
	station_cd = forms.ModelMultipleChoiceField(queryset=Station.objects.all())

StationInMovieFormSet = forms.inlineformset_factory(
	Movie, StationInMovie, fields='__all__', extra=5
)