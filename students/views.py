from django.shortcuts import render

# Create your views here.
def log2(request):
    return render(request,'students/login.html')

def mark1(request):
    return render(request, 'students/viewmarks.html')

def att1(request):
    return render(request, 'students/viewattendance.html')

