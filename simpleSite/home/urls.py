from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout-func/', views.logout_func, name="logout"),
    path('create-group/', views.create_group, name='create_group'),

]