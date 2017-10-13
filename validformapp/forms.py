from django import forms
from django.core import validators

def check_for_a(value):
    if value[0].lower != 'a':
        raise forms.ValidationError('Make needs to start with - a')

class NameForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    verify_email = forms.EmailField(label=)
    text = forms.CharField(widget=forms.Textarea,
                            validators=[validators.MaxLengthValidator(5)])
    def clean(self):
        cleaned_data = super().clean()
        email = clean_data['email']
        vmail = clean_data['verify_email']

        if email != vmail:
            raise forms.ValidationError('Make shure email match.')
        return cleaned_data
