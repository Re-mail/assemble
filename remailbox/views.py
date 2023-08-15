from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from user.models import User
from home.views import hello

# Create your views here.

def mailbox(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            return render(request, 'remailbox/mail_read.html', {'title': request.POST['selected']})
    
        maillist = [ #수신자 계정으로 받은 메일 리스트를 입력합니다
                    {'no':1, 'sender': '보낸사람1', 'time' : '2023.08.13\t12:34', 'title':'[중요]제목1'}, 
                    {'no':2, 'sender': '보낸사람2', 'time' : '2023.08.13\t56:78', 'title':'[중요]제목2'},
                    {'no':3, 'sender': '보낸사람3', 'time' : '2023.08.13\t90:12', 'title':'[중요]제목3'},
                    {'no':4, 'sender': '보낸사람4', 'time' : '2023.08.13\t34:56', 'title':'[중요]제목4'},
                    {'no':5, 'sender': '보낸사람5', 'time' : '2023.08.13\t78:90', 'title':'[중요]제목5'}
        ]
        
        return render(request, 'remailbox/mailbox.html', {'maillist': maillist})
        
    else:
        return redirect('home')
    

def mail_write(request):
    user_content = User.objects.all()
    content = {'user_content' : user_content}
    
    print(content)
    
    return render(request, 'remailbox/mail_write.html', content)

def mail_read(request):
    if request.method == 'POST':
        
        context = {
            'alret':request.POST['readfunc']
        }
        
        if context['alret']=='답장':
            return render(request, 'remailbox/mail_write.html', {'sender':"아무개"})
        elif context['alret']=='전달':
            return render(request, 'remailbox/mail_write.html', {'mailcontent':"전달할 내용", 'title':'전달할 제목'})
        elif context['alret']=='차단':
            return redirect('mailbox')
        elif context['alret']=='삭제':
            return redirect('mailbox')
        else:
            return render(request, 'remailbox/mail_read.html')
    
    return render(request, 'remailbox/mail_read.html')

#def readfunc(request):  #사용자 차단 등 메일 읽기 페이지 기능요소 구현
    
    
