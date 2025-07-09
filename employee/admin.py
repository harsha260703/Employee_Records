
from django.contrib import admin
from .models import Employee

admin.site.register(Employee)


from .models import Child
admin.site.register(Child)
