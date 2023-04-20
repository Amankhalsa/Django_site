from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class Member(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  phone = models.IntegerField(null=True)
  joined_date = models.DateField(null=True)
  
  def __str__(self):
    return f"{self.firstname} {self.lastname}"


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.TextField()
    
class Contact(models.Model):
  name = models.CharField(max_length=255)
  email = models.CharField(max_length=255)
  phone = models.CharField(max_length=255)
  desc = models.CharField(max_length=255)  

  def __str__(self):
    return f"{self.name} {self.email} {self.phone} {self.desc}"