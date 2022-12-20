from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request, 'school_admin/master.html')

def home(request):
    return render(request, 'school_admin/home.html')

def abt(request):
    return render(request, 'school_admin/about.html')

def cont(request):
    return render(request, 'school_admin/contact.html')
    
def menu(request):
    return render(request, 'school_admin/menu.html')