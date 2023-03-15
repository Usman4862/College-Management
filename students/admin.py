from django.contrib import admin
from students.models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ['roll_number', 'first_name', 'last_name', 'join', 'student_class']
    date_hierarchy= 'join'
    save_as= True
    save_as_continue= True
    save_on_top= True
    save_as_bottom= False
    search_fields= ['first_name', 'last_name', 'student_class', 'roll_number']
    preserve_filters= True
    exclude= ['join', 'date_of_birth']

    