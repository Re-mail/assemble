from django.shortcuts import render, redirect
from user.models import User
from .models import UserProfile, UserRemail, Category

def mypage(request):
    return render(request,'mypage/mypage.html')
    
def new_address(request):
    return render(request, 'mypage/new_address.html' )

def profile_view(request):
    if request.method == 'POST':
        user = request.user
        user_profile, created = UserProfile.objects.get_or_create(user=user)
        
        if UserRemail.objects.filter(user_profile=user_profile).count() < 5:
            user_remail = request.POST.get('remail')
            UserRemail.objects.create(user_profile=user_profile, name=user_remail)
            
        return redirect('profile')
    
    return render(request, 'mypage/profile.html')

#다시다시다시다ㅣ다시다ㅣ시
#사용자-remail주소1-카테고리
#사용자-remail주소2-카테고리 이렇게 연결하기