from django.urls import path
from . import views

urlpatterns = [
    path('teacher/list', views.teachers_list, name='teacher-list'),
    path('teacher/add', views.add_teacher, name='teacher-add'),
    path('teacher/delete/<int:id>', views.delete_teacher, name='teacher-delete'),
    path('teacher/view/<int:id>', views.view_teacher, name='teacher-view'),
]
