from django.db import models

class Employee(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"
