from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404,redirect
from Admin.models import *
@login_required
def student_dashboard(request):

    student = get_object_or_404(Student, user=request.user)

    subjects = Subject.objects.filter(assigned_class=student.Grade)

    assignments = Assignment.objects.filter(subject__assigned_class=student.Grade)

    context = {
        "student": student,
        "total_subjects": subjects.count(),
        "total_assignments": assignments.count(),
        "assignments": assignments.order_by("due_date")[:5],
    }

    return render(request, "student_dashboard.html", context)

@login_required
def view_subjects(request):
    student = get_object_or_404(Student, user=request.user)

    subjects = Subject.objects.filter(assigned_class=student.Grade)

    context = {
        "student": student,
        "subjects": subjects
    }
    return render(request, "view_subjects.html", context)


@login_required
def view_assignments(request):
    student = get_object_or_404(Student, user=request.user)

    assignments = Assignment.objects.filter(subject__assigned_class=student.Grade).order_by("due_date")

    context = {
        "student": student,
        "assignments": assignments,
    }
    return render(request, "view_assignments.html", context)

@login_required
def submit_assignment(request, assignment_id):

    student = get_object_or_404(Student, user=request.user)
    assignment = get_object_or_404(Assignment, id=assignment_id)

    if request.method == "POST":
        file = request.FILES.get("file")

        Submission.objects.create(
            assignment=assignment,
            student=student,
            submitted_file=file
        )

        return redirect("student-dashboard")

    return render(request, "submit_assignment.html", {
        "assignment": assignment
    })

@login_required
def view_grade(request, assignment_id):
    student = get_object_or_404(Student, user=request.user)

    assignment = get_object_or_404(Assignment, id=assignment_id)

    submission = Submission.objects.filter(
        assignment=assignment,
        student=student
    ).first()

    return render(request, "view_grade.html", {
        "submission": submission,
        "assignment": assignment
    })
