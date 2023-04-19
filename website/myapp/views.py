from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import get_user_model

from django.template import loader
from .models import Member

# Create your views here.
def myfunctioncall(request):
	User = get_user_model()
	users = User.objects.all()
	return HttpResponse("<h1>hello world this is from my app</h1>")


def add(request,a,b):
	# a=int(input("enter num1"))
	# b=int(input("enter num2"))
	return HttpResponse(f'<h1> You ans is :{a+b}</h1>')
def intro(request,name,age):
	my_dict={
	 'Name':name,
	 'Age':age 
	 }

	return JsonResponse(my_dict)




def members(request):
  mymembers = Member.objects.all().values()
  context = {
    'mymembers': mymembers,
  }
  return render(request,"all_members.html",context) 


def details(request, id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember,
  }
  return HttpResponse(template.render(context, request))

def fruits(request):

  context = {
    'fruits': ['Apple', 'Banana', 'Cherry'],   
  }
#   return JsonResponse(context)
  return render(request,"template.html",context) 