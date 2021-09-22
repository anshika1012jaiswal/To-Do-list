
from django.urls import path
from todoapp import views

urlpatterns = [
path('',views.home,name='home')  ,
path('task',views.task,name='task'),
path('delete/<int:id>',views.delete ,name='delete'),
path('about',views.about,name='about')  
]
