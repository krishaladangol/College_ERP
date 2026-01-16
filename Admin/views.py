from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from datetime import date
# Create your views here.
def add_student(request):
    if request.method=="POST":
        form=Student_form(request.POST)
        if form.is_valid():
            Firstname=form.cleaned_data['Firstname']
            Lastname=form.cleaned_data['Lastname']
            Grade=form.cleaned_data['Grade']

            Student.objects.create(
                Firstname=Firstname,
                Lastname=Lastname,
                Grade=Grade
            )
        else:
            return redirect("add_student")
    else:
        form=Student_form()
    return render(request,"add_student.html",{'form':form})

# def attendance(request):
#     teacher = Subject.objects.get(id=teacher_id)
#     students = Student.objects.filter(Grade=teacher.assigned_class)

#     if request.method == "POST":
#         today = date.today()
#         for student in students:
#             status = request.POST.get(f"status_{student.id}")
#             Attendance.objects.update_or_create(
#                 student=student,
#                 date=today,
#                 defaults={'status': status}
#             )
#         return redirect('attendance', teacher_id=teacher.id)

#     return render(request, "attendance.html", {"students": students, "teacher": teacher})

def teacher_add(request):
    
    if request.method=="POST":
        form=Teacher_add(request.POST)
        if form.is_valid():
            Teacher_name=form.cleaned_data['Teachername']
            subject=form.cleaned_data['Subject']
            Assigned_class=form.cleaned_data['Assignedclass']
            student = Student.objects.filter(Grade=Assigned_class)
            Subject.objects.create(
                
                Teachername=Teacher_name,
                subject=subject,
                assigned_class=Assigned_class
            )
            return redirect("view Teacher")
        else:
            return redirect("Teacher_add")
    else:
        form=Teacher_add()

    return render(request,"add_teacher.html",{'form':form})


def view_teacher(request):
    all_teacher=Subject.objects.all()
    return render(request,"view_teacher.html",{'teachers':all_teacher})

def edit_teacher(request,teacher_id):
    teacher=get_object_or_404(Subject,id=teacher_id)
    if request.method=="POST":
        teacher.Teachername=request.POST.get('Teachername')
        teacher.subject=request.POST.get("Subject")
        teacher.assigned_class=request.POST.get("Assigned_class")
        
        teacher.save()
        return redirect("view_teacher")
    return render(request,"edit_teacher.html",{'teacher':teacher})

def delete_teacher(request,teacher_id):
    teacher=get_object_or_404(Subject,id=teacher_id)

    if request.method=="POST":
        teacher.delete()
        return redirect('view_teacher')
    return render(request,"delete_teacher.html",{'object':teacher})
