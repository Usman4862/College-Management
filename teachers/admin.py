from django.contrib import admin
from teachers.models import Teacher, Salary
# Register your models here.

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display= ['first_name', 'last_name', 'joining_date']
    date_hierarchy = 'joining_date'
    save_as= True
    save_on_top= True
    save_as_continue= True
    save_as_bottom=False
    search_fields= ['first_name', 'last_name', 'teacher_class', 'contact_number']
    preserve_filters= True
    exclude= ['still_joined']

@admin.register(Salary)
class SalaryAdmin(admin.ModelAdmin):
    list_display= ['basic_salary', 'bank']
    save_on_top= True
    search_fields= ['basic_salary', 'bank']
    preserver_filters= True
    exclude= ['date_of_birth']
