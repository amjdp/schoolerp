from django.urls import path
from . import views

urlpatterns = [
    path('student_login', views.log2),
    path('marks', views.mark1),
    path('my_att', views.att1)
]