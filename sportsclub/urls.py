from django.urls import path
from . import views

urlpatterns = [
    path('master_page', views.master),
    path('home_page', views.home),
    path('courses', views.course),
    path('contact_us', views.cont),
    path('menu', views.menu)    
]

