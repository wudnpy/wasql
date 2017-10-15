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
    #objects = Query.objects.all()

    objects = Query.objects.all().values()

    return render(request, 'workspace/queries.html', {'objects':objects})

def query_detail(request, q_id):

    objects = Query.objects.all().values()

    is_queries = True

    query_form = QueryFormType0()

    elements = {'query_form': query_form, 'is_queries': is_queries, }

    for item in request:
        print(item)
    if request.method == 'POST':
        query_form = QueryFormType0(request.POST)

        if query_form.is_valid():
            q_name = query_form.cleaned_data['name']
            elements.update({'q_name': q_name})


            # Обработка значения выбранного пользователем
            for object in objects:
                if str(object['name']) == str(q_name):
                    q_number = object['number']
                    elements.update({'q_number': q_number})
                    q_total_time = object['total_time']
                    elements.update({'q_total_time': q_total_time})
            return redirect('/scauthapp')
    return render(request, 'workspace/query-detail.html', elements)

def rating(request):
    return render(request, 'workspace/rating.html')
