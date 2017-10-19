from django.shortcuts import render

from rating.models import Indicators

# Create your views here.
def rating(request):

    indicators = Indicators.objects.all().values()
    #print(indicators)
    #print('LEN: ' + str(len(indicators)))
    return render(request, 'rating/home.html', { 'indicators': indicators })

def score(request):
    return render(request, 'rating/score.html', {})
