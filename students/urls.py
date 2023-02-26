from django.urls import path
from . import views

urlpatterns = [
    path('student/list', views.student_lists, name='student-list'),
    path('student/add', views.add_student, name='student-add'),
    path('student/delete/<int:id>', views.delete_student, name='delete-student'),
    path('student/view/<int:id>', views.view_student, name='view-student'),
    
]
