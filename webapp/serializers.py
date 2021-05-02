from rest_framework import serializers
from .models import Employees

class EmployeesSerializer(serializers.ModelSerializer):
     class Meta:
         model = Employees
         fields = ( 'first_name', 'last_name', 'emp_id')
         # it will serialize the  mention field data that already mentioned in models.py