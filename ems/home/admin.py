from django.contrib import admin
from . models import Department,Role,Employee
# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','location']
   

admin.site.register(Department,DepartmentAdmin)
   

class RoleAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Role,RoleAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name','dept']

admin.site.register(Employee,EmployeeAdmin)