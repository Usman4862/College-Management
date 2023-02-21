"""College URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from students.views import student_lists, add_student, delete_student, view_student
from teachers.views import teachers_list
from core.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('college/student/list', student_lists, name='student-list'),
    path('college/student/add', add_student, name='student-add'),
    path('college/teacher/list', teachers_list, name='teacher-list'),
    path('', home, name='home'),
    path('college/student/delete/<int:id>', delete_student, name='delete-student'),
    path('college/student/view/<int:id>', view_student, name='view-student'),
]
