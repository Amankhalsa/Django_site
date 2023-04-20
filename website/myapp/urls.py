from django.urls import path
from . import views
urlpatterns=[
	path('preet/',views.myfunctioncall,name='preet'),
	path('add/<int:a>/<int:b>',views.add,name='add'),
	path('intro/<str:name>/<int:age>',views.intro,name='intro'),
	path('members/',views.members,name='members'),
	path('members/details/<int:id>', views.details, name='details'),
	path('fruits/', views.fruits, name='fruits'),
    path('thanks/', views.thanks, name="thank"),




]