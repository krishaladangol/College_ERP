from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from Admin.models import *
@login_required
def student_dashboard(request):

    # Get logged-in student
    student = get_object_or_404(Student, user=request.user)

    # Get subjects for this student's grade
    subjects = Subject.objects.filter(assigned_class=student.Grade)

    # Get assignments for those subjects
    assignments = Assignment.objects.filter(subject__assigned_class=student.Grade)

    context = {
        "student": student,
        "total_subjects": subjects.count(),
        "total_assignments": assignments.count(),
        "assignments": assignments.order_by("due_date")[:5],
    }

    return render(request, "student_dashboard.html", context)
