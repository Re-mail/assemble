from django.shortcuts import render

# Create your views here.

def mailbox(request):
    
    return render(request, 'remailbox/mailbox.html')

def mail_write(request):
    
    return render(request, 'remailbox/mail_write.html')

def mail_read(request):
    
    return render(request, 'remailbox/mail_read.html')
