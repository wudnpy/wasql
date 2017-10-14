from django.shortcuts import render, redirect

from workspace.forms import QueryForm
from workspace.forms import Query

# Create your views here.
def news(request):
    is_news = True
    return render(request, 'workspace/news.html', {
        'is_news': is_news
    })

def queries(request):
    objects = Query.objects.all()
    return render(request, 'workspace/queries.html', {'objects':objects})

def query_detail(request):

    query_form = QueryForm()
    is_queries = True
    elements = {'query_form': query_form, 'is_queries': is_queries, }

    for item in request:
        print(item)
    if request.method == 'POST':
        query_form = QueryForm(request.POST)

        if query_form.is_valid():
            q_name = query_form.cleaned_data['name']
            elements.update({'q_name': q_name})
            objects = Query.objects.all().values()

            # Обработка значения выбранного пользователем
            for object in objects:
                if str(object['name']) == str(q_name):
                    q_number = object['number']
                    elements.update({'q_number': q_number})
                    q_total_time = object['total_time']
                    elements.update({'q_total_time': q_total_time})
            return redirect('/scauthapp')
    return render(request, 'workspace/query_detail.html', {elements})
