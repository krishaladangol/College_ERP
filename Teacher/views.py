from django.shortcuts import render,redirect,get_object_or_404
from Account.forms import LoginForm
from django.contrib.auth import authenticate
from django.contrib import messages
from Admin.models import Student,Teacher,Subject,Assignment,Attendance
from .forms import *
# Create your views here.
def login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
         
            user=authenticate(request,password=password)
            if user is not None:
                login(request,user)
                return redirect('dashboard')
            else:
                messages.error(request,"Username or Password Incorrect")
    else:
        form=LoginForm()        
    return render(request,"Login.html",{'form':form})

def add_assignment(request):
    if request.method == "POST":
        form = AddAssignment(request.POST, request.FILES)
        if form.is_valid():
            Assignment.objects.create(
                teacher=form.cleaned_data['teacher'],
                subject=form.cleaned_data['subject'],
                title=form.cleaned_data["title"],
                description=form.cleaned_data["description"],
                assigned_date=form.cleaned_data["assigned_date"],
                due_date=form.cleaned_data["due_date"],
                total_marks=form.cleaned_data["total_marks"],
                file=form.cleaned_data["file"],
            )
            return redirect('view_assignment')
    else:
        form = AddAssignment()

    return render(request, "add_Assignment.html", {'form': form})

def view_assignment(request):
    student=Assignment.objects.all()
    return render(request,"view_assignment.html",{'all_assignment':student})


   

def teacher_dashboard(request, teacher_id):
    # Get all subjects assigned to this teacher
    subjects = Subject.objects.filter(teacher_id=teacher_id)

    # Total students across all subjects/classes
    total_students = Student.objects.count()

    # Total subjects assigned
    total_subjects = subjects.count()

 


    context = {
        'total_students': total_students,
        'total_subjects': total_subjects,
       
    }

    return render(request, 'teacher_dashboard.html', context)

def profile(request,teacher_id):
    teacher=get_object_or_404(Teacher,TeacherID=teacher_id)
    return render(request,"profile.html",{"teacher":teacher})