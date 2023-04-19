from django.contrib import admin
from .models import Member
from .models import Post


class PostModel(admin.ModelAdmin):
  list_display = ("title", "slug")
admin.site.register(Post,PostModel)

# Register your models here.
# admin.site.register(Member)
class MemberAdmin(admin.ModelAdmin):
  list_display = ("firstname", "lastname", "joined_date","phone")
  
admin.site.register(Member, MemberAdmin)