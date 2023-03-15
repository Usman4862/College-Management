from django.shortcuts import render, redirect, reverse
from teachers.models import Teacher, Salary
# Create your views here.

def teachers_list(request):
    teachers = Teacher.objects.all()
    context = {
        "teachers" : teachers
    }
    return render(request, "teachers_list.html", context= context)
    
def add_teacher(request):
    if request.method == "GET":
        return render(request, "add_teacher.html")
    elif request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        date_of_birth = request.POST["date_of_birth"]
        teacher_class = request.POST["class_"]
        gender = request.POST["GenderChoice"]
        teacher = Teacher.objects.create(
            first_name=first_name,
            last_name=last_name,
            date_of_birth=date_of_birth,
            teacher_class = teacher_class,
            gender = gender,
        )
        teacher.save()
        return redirect(reverse("teacher-list"))

def delete_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    teacher.delete()
    return redirect(reverse('teacher-list'))

def view_teacher(request, id):
    teacher = Teacher.objects.get(id=id)
    context = {
        "teacher" : teacher
    }
    return render(request, "view_teacher.html", context=context)

# this is a comment
