from django.urls import path
from . import views

urlpatterns = [
    path('all_teachers', views.teachers),
    path('all_students', views.students),
    path('login', views.log)
]