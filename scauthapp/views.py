from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

from scauthapp.forms import UserForm, DepartmentForm

# Create your views here.
def home(request):
    return redirect(authapp_home)

@login_required(login_url='/scauthapp/login')
def authapp_home(request):
    is_home = True
    return render(request, 'scauthapp/home.html', {
        'is_home': is_home
    })

def authapp_sign_up(request):
    user_form = UserForm()
    department_form = DepartmentForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        department_form = Department(request.POST, request.FILES)

        if user_form.is_valid() and department_form.is_valid():

            new_user = User.objects.create_user(**user_form.cleaned_data)
            new_department = department_form.save(commit=False) # ??? сохранение без отправки в базу
            new_department.user = new_user
            new_department.save()

            user = authenticate(
                username = user_form.cleaned_data['username'],
                password = user_form.cleaned_data['password']
            )

            login(request, user)

            return redirect(authapp_home)


    return render(request, 'scauthapp/sign_up.html', {
        'user_form': user_form,
        'department_form': department_form
    })
