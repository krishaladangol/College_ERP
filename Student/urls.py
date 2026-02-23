from django.urls import path
from . import views
urlpatterns = [
    path('student_dashboard/',views.student_dashboard,name="student-dashboard"),
    path('view_subjects/',views.view_subjects,name="view-subjects"),
    path('view_assignments/',views.view_assignments,name="view-assignments"),
    path("submit_assignment/<int:assignment_id>/", views.submit_assignment, name="submit-assignment"),
    path("assignment/<int:assignment_id>/grade/",views.view_grade,name="view-grade"),
]