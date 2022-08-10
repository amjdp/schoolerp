from django.shortcuts import render

# Create your views here.
def teachers(request):
    return render(request,'school_admin/viewteachers.html')

def students(request):
    return render(request, 'school_admin/viewstudents.html')

def log(request):
    return render(request, 'school_admin/login.html')