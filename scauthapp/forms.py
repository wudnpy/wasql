from django.contrib.auth.models import User
from django import forms

from scauthapp.models import Department

class UserForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите логин'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    email = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите e-mail'}))


    # используется для изменения label, если переменная задана.
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = 'Логин'
        self.fields['password'].label = 'Пароль'
        self.fields['first_name'].label = 'Имя'
        self.fields['last_name'].label = 'Фамилия'
        self.fields['email'].label = 'Почта'

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')
        # используется для изменения label, если переменная не задана.
        labels = {
            'username': 'Логин',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'email': 'Почта'
        }




class DepartmentForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите название отдела'}))

    def __init__(self, *args, **kwargs):
        super(DepartmentForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Название отдела'


    class Meta:
        model = Department
        fields =  ('name', 'logo')

        labels = {
            'name': 'Отдел',
            'logo': 'Логотип'
        }
