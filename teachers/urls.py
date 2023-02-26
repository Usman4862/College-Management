from django.urls import path
from . import views

urlpatterns = [
    path('teacher/list/', views.teachers_list, name='teacher-list')
]
