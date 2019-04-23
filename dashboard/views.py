from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        'title': 'Dashboard',
    }
    return render(request, 'dashboard/index.html', context)


def buttons(request):
    context = {
        'title': 'Buttons',
    }
    return render(request, 'dashboard/buttons.html', context)


def cards(request):
    context = {
        'title': 'Cards',
    }
    return render(request, 'dashboard/cards.html', context)


def colors(request):
    context = {
        'title': 'Color Utilities',
    }
    return render(request, 'dashboard/colors.html', context)


def border(request):
    context = {
        'title': 'Border Utilities',
    }
    return render(request, 'dashboard/border.html', context)


def animation(request):
    context = {
        'title': 'Animation Utilities',
    }
    return render(request, 'dashboard/animation.html', context)


def other(request):
    context = {
        'title': 'Other Utilities',
    }
    return render(request, 'dashboard/other.html', context)


def login(request):
    context = {
        'title': 'Login',
    }
    return render(request, 'dashboard/login.html', context)


def register(request):
    context = {
        'title': 'Register',
    }
    return render(request, 'dashboard/register.html', context)


def forgot_pwd(request):
    context = {
        'title': 'Forgot Password',
    }
    return render(request, 'dashboard/forgot-password.html', context)


def blank(request):
    context = {
        'title': 'Blank Page',
    }
    return render(request, 'dashboard/blank.html', context)


def error(request):
    context = {
        'title': '404 Page',
    }
    return render(request, '404.html', context)


def charts(request):
    context = {
        'title': 'Charts',
    }
    return render(request, 'dashboard/charts.html', context)


def tables(request):
    context = {
        'title': 'Tables',
    }
    return render(request, 'dashboard/tables.html', context)
