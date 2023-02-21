from django.shortcuts import render, redirect, reverse
from students.models import Student
from College import urls
# Create your views here.
def student_lists(request):
    # students = Student.objects.all()
    students = Student.objects.filter(pass_matric=True)
    # students = Student.objects.filter(roll_number=2, first_name="Usman")
    # students = Student.objects.filter(fee=10000)
    context = {
        "students" : students
    }
    return render(request, "students_list.html", context=context)

def add_student(request):
    if request.method == "GET":
        return render(request, "add_student.html")
    elif request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        date_of_birth = request.POST["date_of_birth"]
        fee = request.POST["fee"]
        roll_number = request.POST["roll_number"]
        student_class = request.POST["student_class"]
        if Student.id == roll_number:
            return render(request, "error.html")
        else:
            student = Student.objects.create(
                first_name=first_name,
                last_name=last_name,
                date_of_birth=date_of_birth,
                fee=fee,
                roll_number=roll_number,
                student_class=student_class
            )
            student.save()
            return redirect(reverse('student-list'))

def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    return redirect(reverse('student-list'))

def view_student(request, id):
    student = Student.objects.get(id=id)
    context = {
        'student' : student
    }
    return render(request, 'view_student.html', context=context)
        



    



        
    
