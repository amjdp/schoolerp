from django.shortcuts import render

# Create your views here.
def log2(request):
    return render(request,'students/login.html')

def mark1(request):
    return render(request, 'students/viewmarks.html')

def att1(request):
    return render(request, 'students/viewattendance.html')

def hm(request):
    return render(request, 'students/baabtra_home.html')

def cou(request):
    return render(request, 'students/baabtra_courses.html')

def cont(request):
    return render(request, 'students/baabtra_contact_us.html')

def master(request):
    return render(request, 'students/master_page.html')

