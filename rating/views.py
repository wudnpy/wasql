from django.shortcuts import render


from rating.models import Indicators
from rating.models import Ac

# Create your views here.
def rating(request):

    indicators = Indicators.objects.all().values()
    #print(indicators)
    #print('LEN: ' + str(len(indicators)))
    return render(request, 'rating/home.html', { 'indicators': indicators })

def score(request):

    ac_all = Ac.objects.all()

    # months = {
    #     'name': 'Январь', 'name': 'Февраль', 'name': 'Март', 'name': 'Апрель',
    #     'name': 'Май', 'name': 'Июнь', 'name': 'Июль', 'name': 'Август',
    #     'name': 'Сентябрь', 'name': 'Октябрь', 'name': 'Ноябрь', 'name': 'Декабрь'
    # }

    months = [
        "Январь", "Февраль", "Март", "Апрель",
        "Май", "Июнь", "Июль", "Август",
        "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"
    ]

    groups = [
        "Выполнение плана по Гос. Заданию", "Использование Аналитических систем",
        "Использование медицинского оборудования", "Использование технического оборудования",
        "Кадровая аналитика", "Качество ведения приема", "Льготное лекарственное обеспечение",
        "Нарушения", "Обеспеченность кадрами", "Профилактическая работа", "Соблюдение МСП",
        "Управление финансами", "Уровень смертности"
    ]

    age = [
        "Взрослые", "Дети"
    ]


    print(months)
    print('LEN: ' + str(len(ac_all)))

    return render(request, 'rating/score.html', {'ac_all': ac_all, 'months': months, 'groups': groups, 'age': age})
