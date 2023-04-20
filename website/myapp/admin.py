from django.contrib import admin
from .models import Member
from .models import Contact

from .models import Post


class PostModel(admin.ModelAdmin):
  list_display = ("title", "slug")
admin.site.register(Post,PostModel)

# Register your models here.
class ContactModel(admin.ModelAdmin):
  list_display = ("name", "email", "phone", "desc")
admin.site.register(Contact,ContactModel)

class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone")
  
admin.site.register(Member, MemberAdmin)
