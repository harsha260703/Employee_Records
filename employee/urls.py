from django.urls import path
from . import views

urlpatterns = [
    path('', views.employee_list, name='employee_list'),
    path('register/', views.register_employee, name='register_employee'),
]
