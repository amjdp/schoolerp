from django.urls import path
from . import views

urlpatterns = [
    path('home_page', views.home, name='p1'),
    path('about_us', views.abt, name='p2'),
    path('contact_us', views.cont, name='p3'),
    path('menu', views.menu, name='p4'),
    path('master_page', views.master, name='p5')
]



# path('all_teachers', views.teachers),
#     path('all_students', views.students),
#     path('login', views.log)