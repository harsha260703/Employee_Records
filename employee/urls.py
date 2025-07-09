from django.urls import path
from . import views



urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('register/', views.register_employee, name='register_employee'),
    path('children/', views.child_list, name='child_list'),
    path('children/register/', views.register_child, name='register_child'),
]
