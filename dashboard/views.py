from django.shortcuts import render

# Create your views here.

def index(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'dashboard/index.html', context)

def blank(request):
    context = {
        'title': 'Blank Page',
    }
    return render(request, 'dashboard/blank.html', context)