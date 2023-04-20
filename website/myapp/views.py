from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.contrib.auth import get_user_model

from django.template import loader
from .models import Member
from .models import Contact
from django.core.mail import EmailMessage
from django.contrib import messages
MESSAGE_TAGS = {
        messages.DEBUG: 'alert-secondary',
        messages.INFO: 'alert-info',
        messages.SUCCESS: 'alert-success',
        messages.WARNING: 'alert-warning',
        messages.ERROR: 'alert-danger',
}
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

def thanks(request):
    if request.method =='POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # context = {
        #     'name': name, 'email':email , 'phone':phone, 'desc':desc
        # }

        Contact.objects.create(
        name= request.POST['name'],
        email= request.POST['email'],
        phone= request.POST['phone'],
        desc= request.POST['desc']

      )
        EmailMessage(
                'Django Contact Form {}'.format(name),
                'Hi ' +name+
                '\n\n'+
                'Message:'+ desc+
                '\n\n' +
                'Phone number : '+phone,
                f'form-{email}', # Send from (your website)
                ['digamber@yopmail.com'], # Send to (your admin email)
                [],
                reply_to=[email] # Email from the form to get back to
            ).send()  
    messages.success(request, 'Contact Form submitted successfully.')
    return render(request,"contact.html")