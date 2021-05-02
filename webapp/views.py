from django.shortcuts import render
from django.http import HttpResponse
#from django.shortcuts import get_object_or_404   #its is used when requested object doesnot exist
from rest_framework import viewsets             #it is used to return data
#from rest_framework.response import Response     # its is used to return response that everything is fine like 200
#from rest_framework import status                
from .serializers import EmployeesSerializer
from .models  import Employees



class EmployeesView(viewsets.ModelViewSet):    
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer
         