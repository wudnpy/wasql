from django.conf.urls import url
from testurlapp import views

urlpatterns = [
    # Варианты регулярных выражений, которые должны совпадать с
    # путями в браузере пользователей, чтобы получить страницу.

    # site.com/user/12
    #url(r'^user/(\d+)/$', views.home, name='home'),

    # site.com/user/12/2000
    #url(r'^user/(\d{2})/(\d{4})/$', views.home, name='home'),


    # Запись значений в переменные
    # site.com/
    url(r'^user/(?P<month>\d{2})/(?P<year>\d{4})/$', views.home, name='home'),

]
