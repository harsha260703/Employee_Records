from django.urls import path
from . import views



urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('register/', views.register_employee, name='register_employee'),
    path('children/', views.child_list, name='child_list'),
    path('children/register/', views.register_child, name='register_child'),
    path('students/register/', views.register_student, name='register_student'),
    path('students/', views.student_list, name='student_list'),

]
