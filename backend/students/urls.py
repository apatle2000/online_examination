#from django.contrib import admin
from django.urls import path
from . import views


app_name = "students" 


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.students, name='students_page'),
]
