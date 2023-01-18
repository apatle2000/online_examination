#from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse

#accessing the databse 
# from django.db.migrations.recorder import MigrationRecorder
#from login.models import Person
# latest_migration = MigrationRecorder.Migration.objects.all()
# ss=""
# for i in latest_migration:
#     ss=ss+str(i)+"\n\n"



def Home(request):
    #instances  = Person.objects.all().values()
    return JsonResponse({
        "persons": list()#instances)
    })

