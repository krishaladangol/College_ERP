from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from datetime import date
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

###Admin

# Teacher View

def teacher_add(request):
    if request.method == "POST":
        form = Teacher_add(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            teacher_name = form.cleaned_data['Teachername']
            subject_name = form.cleaned_data['Subject_name']
            assigned_class = form.cleaned_data['Assignedclass']
            teacher_id = form.cleaned_data['Teacherid']
            department = form.cleaned_data['department']
            password = form.cleaned_data['password']

            # Check if user exists
            user, user_created = User.objects.get_or_create(username=username)

            if user_created:
                user.set_password(password)
                user.save()

            # Check if teacher profile exists
            teacher, teacher_created = Teacher.objects.get_or_create(
                user=user,
                defaults={
                    "TeacherID": teacher_id,
                    "Teachername": teacher_name,
                    "department": department
                }
            )

            Subject.objects.create(
                teacher=teacher,
                subject_name=subject_name,
                assigned_class=assigned_class
            )

            return redirect("view_teacher")

    else:
        form = Teacher_add()

    return render(request, "add_teacher.html", {"form": form})


def view_teacher(request):
    teachers = Teacher.objects.all()
    subjects = Subject.objects.select_related('teacher')
    return render(request,"view_teacher.html",{'subjects':subjects,'teacher':teachers})

def edit_teacher(request,teacher_id):
    teacher = get_object_or_404(Teacher, TeacherID=teacher_id)
    subject = Subject.objects.filter(teacher=teacher).first() 
    if request.method=="POST":
        teacher.Teachername = request.POST.get('Teachername')
        teacher.department = request.POST.get('department', teacher.department)
        teacher.save()
        if subject:
            subject.subject_name = request.POST.get("Subject", subject.subject_name)
            subject.assigned_class = request.POST.get("Assigned_class", subject.assigned_class)
            subject.save()
        return redirect("view_teacher")
    return render(request,"edit_teacher.html",{'subject':subject})

def delete_teacher(request,teacher_id):
    teacher=get_object_or_404(Teacher,TeacherID=teacher_id)

    if request.method=="POST":
        teacher.user.delete()
        return redirect('view_teacher')
    return render(request,"delete_teacher.html",{'object':teacher})


# student View

def add_student(request):
    if request.method == "POST":
        form = Student_form(request.POST)

        if form.is_valid():
            Firstname = form.cleaned_data['Firstname']
            Lastname = form.cleaned_data['Lastname']
            Grade = form.cleaned_data['Grade']
            Course = form.cleaned_data['Course']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if User.objects.filter(username=username).exists():
                form.add_error('username', 'Username already exists')
            else:
                user = User.objects.create_user(
                    username=username,
                    password=password
                )

                Student.objects.create(
                    user=user,
                    Firstname=Firstname,
                    Lastname=Lastname,
                    Grade=Grade,
                    course=Course,
                )

                return redirect("view_student")

    else:
        form = Student_form()

    return render(request, "add_student.html", {'form': form})


def view_student(request):
    student=Student.objects.all()
    return render(request,"view_student.html",{'all_student':student})

def edit_student(request,student_id):
    student=get_object_or_404(Student,id=student_id)
    if request.method=="POST":
        student.Firstname=request.POST.get('Firstname')
        student.Lastname=request.POST.get('Lastname')
        student.Grade=request.POST.get('Grade')
        student.course=request.POST.get('Course')

        student.save()
        return redirect('view_student')
    return render(request,"edit_student.html",{'student':student})

def delete_student(request,student_id):
    student=get_object_or_404(Student,id=student_id)
    if request.method=="POST":
        student.user.delete()
        return redirect("view_student")
    return render(request,"delete_student.html",{'student':student})

# def admin_login(request):
#     if not request.user.is_authenticated:
#         return redirect("Login")
#     return render(request,"Home.html")

@login_required
def dashboard(request):
    if not request.user.is_staff:
        return redirect('login')    
    context={
        "students":Student.objects.count(),
        "teachers":Teacher.objects.count(),
        
    }
    return render(request,"dashboard.html",context)