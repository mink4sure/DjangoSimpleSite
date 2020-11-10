from django.urls import path
from . import views


app_name = 'welkom'
urlpatterns = [
    path('', views.welkom, name='welkom'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('AddUser/', views.AddUser, name='AddUser'),
]