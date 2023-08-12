from django.shortcuts import render, redirect
from django.db import transaction
from .models import Signup
from argon2 import PasswordHasher
from .forms import RegisterForm

# Create your views here.
def signup(request):
    signup_form = RegisterForm()
    context = {'forms' : signup_form}

    if request.method == 'GET':
        return render(request, 'signup/signup.html', context)

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
        return render(request, 'signup/signup.html',context)