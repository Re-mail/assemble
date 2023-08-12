from django.shortcuts import render, redirect
from django.db import transaction
from .models import Signup
from argon2 import PasswordHasher
from .forms import RegisterForm, LoginForm

# Create your views here.
def signup(request):
    signup_form = RegisterForm()
    context = {'forms' : signup_form}

    if request.method == 'GET':
        return render(request, 'user/signup.html', context)

    elif request.method =='POST':
        signup_form = RegisterForm(request.POST)
        if signup_form.is_valid():
            person = Signup(
                person_email = signup_form.person_email,
                person_pw = signup_form.person_pw
            )
            person.save()
            return redirect('/')
        else:
            context['forms'] = signup_form
            if signup_form.errors:
                for value in signup_form.errors.values():
                    context['error'] = value
        return render(request, 'user/signup.html',context)
    

def login(request):
    login_form = LoginForm()
    context = {'forms' : login_form}

    if request.method == 'GET':
        return render(request, 'user/login.html',context)
    elif request.method == 'POST':
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            # request.session['login_session'] = login_form.login_session
            # request.session.set_expiry(0)
            return redirect('/')
        else:
            context['forms'] = login_form
            if login_form.errors:
                for value in login_form.errors.values():
                    context['error'] = value
        return render(request, 'user/login.html',context)
    