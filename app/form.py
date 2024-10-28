from django import forms
from app.models import *
class TopicForms(forms.Form):
    tn = forms.CharField()
class Webforms(forms.Form):
    table_name = forms.ModelChoiceField(queryset=Topic.objects.all())
    name = forms.CharField()
    url = forms.URLField()
    email = forms.EmailField()


    