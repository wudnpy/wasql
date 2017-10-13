from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower != 'a':
        raise forms.ValidationError('Make needs to start with - a')

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea,
                            validators=[validators.MaxLengthValidator(5)])
