from django.shortcuts import render

from app1.models import table1, table2


# Create your views here.
def home(request):
    obj= table1.objects.all()
    obj2= table2.objects.all()
    return render(request,'index.html',{'result':obj ,'result2':obj2})