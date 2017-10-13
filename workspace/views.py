from django.shortcuts import render

from workspace.forms import QueryForm
from workspace.forms import Query

# Create your views here.
def news(request):
    return render(request, 'workspace/news.html')

def queries(request):

    query_form = QueryForm()
    elements = {'query_form': query_form}
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

    return render(request, 'workspace/queries.html', elements)
