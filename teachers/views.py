from django.shortcuts import render

# Create your views here.
def log1(request):
    return render(request,'teachers/login.html')

def att(request):
    return render(request, 'teachers/addattendance.html')

def marks(request):
    return render(request, 'teachers/addmarks.html')

def student1(request):
    return render(request,'teachers/students.html')

def master(request):
    return render(request,'teachers/masterpage.html')
