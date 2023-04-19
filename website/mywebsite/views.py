# import time
# from django.http import HttpResponse
# def home(request):
#     return HttpResponse('<h1>This is a http response</h1>')
from django.shortcuts import render,HttpResponse
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.template import loader
def home(request):
    return render(request,"index.html")
def contact(request):
    return render(request,"contact.html")
def thanks(request):
    return render(request,"thx.html")
def mypage(request):
    return render(request,"mypage.html")
def about(request):
    return render(request,"about.html")

# Create your views here.
def getUsers(request):

    users = User.objects.all()

    return HttpResponse(f'<h1>This is a http response</h1>{len(users)}')



