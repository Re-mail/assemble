from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def mailbox(request):
    
    return render(request, 'remailbox/mailbox.html')

def mail_write(request):
    
    return render(request, 'remailbox/mail_write.html')

def mail_read(request):
    if request.method == 'POST':
        
        #messages.add_message(request, request.POST['readfunc'])
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
    
    
