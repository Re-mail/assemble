from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.models import User  
from django.contrib import messages
from django.db.utils import IntegrityError
from .models import User  


def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    
    elif request.method == "POST":
        if 4 > len(request.POST["username"]) or len(request.POST["username"]) > 20:
            return render(request, "user/register.html", {"data": "id_too"})
        if request.POST["password1"] == request.POST["password2"]:
            if 5 > len(request.POST["password1"]) or len(request.POST["password1"]) > 15:
                return render(request, "user/register.html", {"data": "password_too"})
            try:
                user = User.objects.create_user(username=request.POST["username"],
                                                password=request.POST["password1"],
                                                email=request.POST["email"])
            except IntegrityError:
                return render(request, "user/register.html", {"data": "id_overlap"})
            auth.login(request, user)
            messages.info(request, "회원가입이 완료되었습니다!")
            return redirect("/home/")
        else:
            return render(request, "user/register.html", {"data": "check_not_same"})
        

# def login(request):
#     loginform = LoginForm()
#     context = {'forms' : loginform}

#     if request.method == 'GET':
#         return render(request, 'user/login.html', context)
    
#     elif request.method == 'POST':
#         loginform = LoginForm(request.POST)

#         if loginform.is_valid(): #로그인 성공 시
#             request.session['login_session'] = loginform.login_session
#             request.session.set_expiry(0)
#             return redirect('mailbox') #mailbox로 이동
#         else:
#             context['forms'] = loginform
#             if loginform.errors:
#                 for value in loginform.errors.values():
#                     context['error'] = value
#         return render(request, 'uesr/login.html', context)
# #수정  
# def logout(request):
#     request.session.flush()
#     return redirect('/')