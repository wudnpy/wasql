from django.shortcuts import render

# Create your views here.
def rating(request):
    return render(request, 'rating/home.html')
