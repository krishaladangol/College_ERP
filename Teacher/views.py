from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from Account.forms import LoginForm
from django.contrib.auth import authenticate,login
from django.contrib import messages
from Admin.models import Student,Teacher,Subject,Assignment,Attendance,Submission
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.
# def Teacherlogin(request):
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data["username"]
#             password=form.cleaned_data["password"]
         
#             user=authenticate(request,username=username,password=password)
#             if user is not None:
#                 login(request,user)
#                 return redirect('dashboard')
#             else:
#                 messages.error(request,"You are not authorized as a teacher")
#     else:
#         form=LoginForm()        
#     return render(request,"Login.html",{'form':form})
@login_required
def add_assignment(request):
    teacher=Teacher.objects.get(user=request.user)
    if request.method == "POST":

        form = AddAssignment(request.POST, request.FILES)
        if form.is_valid():
            Assignment.objects.create(
                teacher=teacher,
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
        form.fields['subject'].queryset=Subject.objects.filter(teacher=teacher)#shows only the teacher assigned subjects
    return render(request, "add_Assignment.html", {'form': form})


@login_required
def view_assignment(request):
    teacher = Teacher.objects.get(user=request.user)
    assignments = Assignment.objects.filter(teacher=teacher)

    return render(request, "view_assignment.html", {
        'all_assignment': assignments
    })

   
@login_required
def teacher_dashboard(request):
    teacher = get_object_or_404(Teacher, user=request.user)
    subjects = Subject.objects.filter(teacher=teacher)
    total_subjects = subjects.count()
    teacher_classes=subjects.values_list('assigned_class', flat=True)
    total_students=Student.objects.filter(Grade__in=teacher_classes).distinct().count()
    assignments = Assignment.objects.filter(teacher=teacher)
    total_assignments = assignments.count()
    


    context = {
        'total_students': total_students,
        'total_subjects': total_subjects,
        'total_assignment':total_assignments,
       
    }

    return render(request, 'teacher_dashboard.html', context)

def profile(request,teacher_id):
    teacher=get_object_or_404(Teacher,TeacherID=teacher_id)
    return render(request,"profile.html",{"teacher":teacher})

@login_required
def view_submissions(request, assignment_id):
    teacher = get_object_or_404(Teacher, user=request.user)
    assignment = get_object_or_404(Assignment, id=assignment_id, teacher=teacher)

    submissions = Submission.objects.filter(assignment=assignment)

    return render(request, "view_submissions.html", {
        "assignment": assignment,
        "submissions": submissions
    })


@login_required
def grade_submission(request, submission_id):
    teacher = get_object_or_404(Teacher, user=request.user)
    submission = get_object_or_404(Submission, id=submission_id)

    if submission.assignment.teacher != teacher:
        return HttpResponse("Unauthorized", status=403)

    if request.method == "POST":
        submission.marks_obtained = request.POST.get("marks")
        submission.feedback = request.POST.get("feedback")
        submission.save()

        return redirect("view-submissions", assignment_id=submission.assignment.id)

    return render(request, "grade_submission.html", {
        "submission": submission
    })
