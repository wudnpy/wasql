from django.contrib.auth.models import User
from django import forms

from scauthapp.models import Department

class UserForm(forms.ModelForm):
    email = forms.CharField(max_length=100, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields =  ('name', 'logo')
