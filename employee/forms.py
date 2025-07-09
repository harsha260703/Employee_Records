from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'employee_id', 'designation', 'department']

from .models import Child

class ChildForm(forms.ModelForm):
    class Meta:
        model = Child
        fields = ['name', 'child_id', 'age', 'gender', 'student_class']

from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'student_id', 'age', 'gender', 'course']

