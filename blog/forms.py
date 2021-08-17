from django.forms import ModelForm
from .models import Movie, Actor
from django import forms

class CreateMovie(ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'content','category','image','year','actors']
class CreateActor(ModelForm):
    class Meta:
        model = Actor
        fields = ['name', 'birthYear', 'description', 'image', 'movies']
class CreateReview(forms.Form):
    context = forms.Textarea()

class CreateRating(forms.Form):
    Numbers = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
        (6, 6),
        (7, 7),
        (8, 8),
        (9, 9),
        (10, 10),

    )
    rating = forms.ChoiceField(widget=forms.RadioSelect, choices=Numbers)


