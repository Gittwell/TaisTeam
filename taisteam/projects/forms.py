from datetime import date
from django import forms
from django.forms import ModelForm

from .models import Project, LettersTais


class AddLettersTais(ModelForm):

    class Meta:
        model = LettersTais
        fields = ['notification', 'project', 'content', 'to_whom', 'date', 'worker']
        widgets = {
            'notification': forms.TextInput(attrs={'class': "form-control", "placeholder": '337КБ/24'}),
            'project': forms.Select(attrs={'class': "form-control"}),
            'content': forms.TextInput(attrs={'class': "form-control"}),
            'to_whom': forms.TextInput(attrs={'class': "form-control"}),
            'date': forms.TextInput(attrs={'class': "form-control"}),
            'worker': forms.TextInput(attrs={'class': "form-control"}),
        }
    # notification = forms.CharField(max_length=10)
    # project = forms.ModelChoiceField(queryset=Project.objects.all())
    # content = forms.CharField(max_length=255)
    # to_whom = forms.CharField(max_length=30)
    # worker = forms.CharField(max_length=30)