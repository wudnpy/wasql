from django import forms

from workspace.models import Query

class QueryForm(forms.ModelForm):
    name = forms.ModelChoiceField(queryset=Query.objects.all())
    class Meta:
        model = Query
        fields = ('name',)
