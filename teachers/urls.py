from django.urls import path
from . import views

urlpatterns = [
    path('teacher_login', views.log1, name='path1'), 
    path('add_att', views.att, name='path2'),
    path('add_mark', views.marks, name='path3'),
    path('view_students', views.student1, name='path4'),
    path('masterpg', views.master, name='path5')
]