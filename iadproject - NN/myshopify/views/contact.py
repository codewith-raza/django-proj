from django.views import View
from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.views import View
from django.core.mail import send_mail
from django.conf import settings


import json
class Contact(View):
    def post(self,request):
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        #print(name,email,phone,desc)
        mydict={'Sender_Email':email, 'Sender_Name':name, 'Sender_Contact':phone,'Message':desc}
        mydict2=json.dumps(mydict, indent=4)
        send_mail('InquiryMail',mydict2,email,['b17101072.dummy@gmail.com'],    fail_silently=False)
        print(send_mail)
        return render(request,'order/contact.html')
    def get(self,request):
        return render(request,'order/contact.html')
