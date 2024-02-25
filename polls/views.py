
from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime
from polls.models import Hire
from django.contrib import messages

def home(request):
    return render(request,"index.html")

def resume(request):
    return render(request, "resume.html")
  
def hire(request):
    if request.method == 'POST':
        mail = request.POST.get('mail') 
        desc = request.POST.get('desc')
        hire = Hire(mail=mail, desc=desc)
        hire.save()
        messages.success(request,'Your Query Has been Submitted')
        return render(request, "hire.html")
    return render(request,"hire.html")

