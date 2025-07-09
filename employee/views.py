from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Register new employee
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/register.html', {'form': form})

# List employees
def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee/employee_list.html', {'employees': employees})
# views.py

from .forms import ChildForm
from .models import Child

# Register new child
def register_child(request):
    if request.method == 'POST':
        form = ChildForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('child_list')
    else:
        form = ChildForm()
    return render(request, 'employee/register_child.html', {'form': form})

# List children
def child_list(request):
    children = Child.objects.all()
    return render(request, 'employee/child_list.html', {'children': children})
