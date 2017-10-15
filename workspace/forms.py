from django import forms

from workspace.models import Query

class QueryFormType0(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Query.objects.filter(number=1))
    class Meta:
        model = Query
        fields = ('name',)
