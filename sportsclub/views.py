from django.shortcuts import render

# Create your views here.
def master(request):
    return render(request, 'sportsclub/master_page.html')

def home(request):
    return render(request, 'sportsclub/home_page.html')

def course(request):
    return render(request, 'sportsclub/about.html')

def cont(request):
    return render(request, 'sportsclub/contact.html')
    
def menu(request):
    return render(request, 'sportsclub/menu.html')

