from django.db import models

class Employee(models.Model):
    serial_number = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=50, unique=True)
    designation = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.employee_id})"

class Child(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    child_id = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    student_class = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name} ({self.child_id})"

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]

    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=50, unique=True)
    age = models.IntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    course = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.student_id})"
