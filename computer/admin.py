from django.contrib import admin

from employee.models import Department, Employee, Room

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(Room)
