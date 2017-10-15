from django.shortcuts import render, redirect

from workspace.forms import QueryFormType0
from workspace.forms import Query

# Create your views here.
def news(request):
    is_news = True
    return render(request, 'workspace/news.html', {
        'is_news': is_news
    })

def queries(request):
    is_queries = True

    objects = Query.objects.all().values()

    return render(request, 'workspace/queries.html', {'objects':objects, 'is_queries':is_queries})

def query_detail(request, q_id):
    is_queries = True # переменная служит для выделения раздела в котором мы находимся на сайте.

    elements = { 'is_queries': is_queries }

    q_object = Query.objects.filter(number=q_id).values()

    elements.update(q_object[0])

    if request.method == 'POST':

        q = request.POST
        print(q.get('name'))
        return redirect('/scauthapp')
    return render(request, 'workspace/query-detail.html', elements)

def rating(request):
    return render(request, 'workspace/rating.html')
