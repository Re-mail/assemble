from django.shortcuts import render, redirect
from django.contrib import auth
#from django.contrib.auth.models import User  
from django.contrib import messages
from django.db.utils import IntegrityError
from .models import User  
from django.contrib.auth import login as auth_login # login함수와 이름이 겹쳐서
import re

def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    
    elif request.method == "POST":
        if User.objects.filter(email=request.POST["email"]).exists():
            return render(request, "user/register.html", {"data": "email_overlap"})
        
        if 2 > len(request.POST["username"]) or len(request.POST["username"]) > 20:
            return render(request, "user/register.html", {"data": "id_too"})
        
        if not check_pw(request.POST["password1"]):
                return render(request, "user/register.html", {"data": "check_wrong_combination"})
            
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
            return redirect('/home/')
        else:
            return render(request, "user/register.html", {"data": "check_not_same"})

def check_pw(password):
    PT1 = re.compile('^(?=.*[A-Z])(?=.*[a-z])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT2 = re.compile('^(?=.*[A-Z])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$')
    PT3 = re.compile('^(?=.*[A-Z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT4 = re.compile('^(?=.*[a-z])(?=.*\d)[A-Za-z\d!@#$%^&*]{8,}$')
    PT5 = re.compile('^(?=.*[a-z])(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$') 
    PT6 = re.compile('^(?=.*\d)(?=.*[!@#$%^&*])[A-Za-z\d!@#$%^&*]{8,}$')
    PT7 = re.compile('^[A-Za-z\d!@#$%^&*]{10,}$')

    for pattern in [PT1,PT2,PT3,PT4,PT5,PT6,PT7]:
        if pattern.match(password):
            return True
        return False
    
def login(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 정보 가져와서 
        email = request.POST['email']
        password = request.POST['password']
        # 로그인
        user = auth.authenticate(request, email=email, password=password)
        # 성공
        if user is not None:
            auth.login(request, user)
            return render(request, 'home/index.html')
        # 실패
        else:
            return render(request, 'user/login.html', {'error': 'incorrect'})
    else:
        return render(request, 'user/login.html')

def logout(request):
    # 포스트 방식으로 들어오면
    if request.method == 'POST':
        # 유저 로그아웃
        auth.logout(request)
        return redirect('home')
    return render(request, 'user/signup.html')

# # Create your views here.
# def login(request) : 
#     if request.method=='POST' :
#         # data는 forms.form 두번쨰 인자이므로 data = 은 생략 가능
#         form = AuthenticationForm(request, data = request.POST) # 먼저 request 인자를 받아야함
#         if form.is_valid() :
#             # 세션 CREATE/ form.get_user는 User 객체 반환
#             auth.login(request, form.get_user())
#             return redirect('/remailbox/') # 로그인 성공시 remailbox 이동
#         else :
#             return render(request, "user/login.html")
#     else :
#         form = AuthenticationForm()
#         context = {
#             'form' : form,
#         }
#         return render(request, "user/login.html", context)
     
# def logout(request):
#     logout(request)
#     messages.success(request, "로그아웃 완료")
#     return redirect('home')
