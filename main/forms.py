from django import forms
from .models import MainDB

class mainForm(forms.ModelForm):
    class Meta:
        model = MainDB
        fields = ['name1', 'name2']