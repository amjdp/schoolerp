from django.urls import path
from . import views

urlpatterns = [
    path('student_login', views.log2, name='q1'),
    path('marks', views.mark1, name='q2'),
    path('my_att', views.att1, name='q3'),
    path('home_page', views.hm, name='q4'),
    path('courses', views.cou, name='q5'),
    path('contact_us', views.cont, name='q6'),
    path('master_page', views.master, name='q7')
]