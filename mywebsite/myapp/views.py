from django.shortcuts import render
from django.http import HttpResponse,JsonResponse


# Create your views here.
def myfunctioncall(request):
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