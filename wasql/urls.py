"""wasql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

from scauthapp import views as sc_auth
from workspace import views as sc_workspace
from rating import views as sc_rating

from scauthapp import forms as sc_auth_forms

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', sc_auth.home, name='home'),
    url(r'scauthapp/login/$', auth_views.login,
        {'template_name': 'scauthapp/login.html', 'authentication_form': sc_auth_forms.LoginForm },
        name='scauthapp-login'),
    url(r'scauthapp/logout/$', auth_views.logout,
        {'next_page': '/'},
        name='scauthapp-logout'),
    url(r'^scauthapp/$', sc_auth.authapp_home, name='scauthapp-home'),
    url(r'^scauthapp/sign-up/', sc_auth.authapp_sign_up, name='scauthapp-sign-up'),
    url(r'^workspace/news/', sc_workspace.news, name='workspace-news'),
    url(r'^workspace/queries/', sc_workspace.queries, name='workspace-queries'),
    url(r'^workspace/query-detail/(\d+)', sc_workspace.query_detail, name='workspace-query-detail'),
    url(r'^rating/home/', sc_rating.rating, name='rating-home'),
    url(r'^rating/score/', sc_rating.score, name='rating-score'),
    #url(r'formpage/', views.form_page, name='form-page')
    #url(r'^(?P<pizza_id>\d+)$', views.pizza_detail, name='pizza-detail'),
    #url(r'^$', views.home, name='index'),
    #url(r'^test_app/', include('testurlapp.test_urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
