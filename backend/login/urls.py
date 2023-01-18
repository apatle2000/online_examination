from django.urls import path
from . import views

app_name = "login" 

urlpatterns = [
     path('', views.login),
     path('get_data/', views.get_data),
     path('add_user/', views.add_user),
]