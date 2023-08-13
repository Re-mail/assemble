from django.shortcuts import render

# Create your views here.

def mypage(request):
    return render(
        request,
        'mypage/mypage.html'
    )
    
def new_address(request):
    return render(
        request,
        'mypage/new_address.html'
    )