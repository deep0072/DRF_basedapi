from django.db import models

class Employees(models.Model):
    first_name = models.CharField(max_length = 50)
    last_name =  models.CharField(max_length = 50)
    emp_id = models.IntegerField()

    def __str__(self):
        return self.first_name  