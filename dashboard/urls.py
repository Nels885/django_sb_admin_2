from django.urls import path

from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.index, name='index'),
    path('buttons/', views.buttons, name='buttons'),
    path('cards/', views.cards, name='cards'),
    path('colors/', views.colors, name='colors'),
    path('border/', views.border, name='border'),
    path('animation/', views.animation, name='animation'),
    path('other/', views.other, name='other'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('password/', views.forgot_pwd, name='password'),
    path('blank/', views.blank, name='blank'),
    path('error/', views.error, name='error'),
    path('charts/', views.charts, name='charts'),
    path('table/', views.tables, name='tables'),
]
