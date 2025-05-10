from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        exclude = ['user', 'Creation_date', 'No_of_songs']