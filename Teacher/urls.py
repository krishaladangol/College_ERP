from django.urls import path
from . import views
urlpatterns = [
    # path('teacherlogin',views.Teacherlogin,name="Login"),
    path('teacherdashboard',views.teacher_dashboard,name="teacher-dashboard"),
    path('profile/<str:teacher_id>',views.profile,name="profile"),
    path('add_assignment',views.add_assignment,name="add_assignment"),
    path('view_assignment',views.view_assignment,name='view_assignment'),
    path('assignment/<int:assignment_id>/submissions',views.view_submissions,name='view-submissions'),

    path('submission/<int:submission_id>/grade',views.grade_submission,name='grade-submission'),
    path('attendance/<int:subject_id>', views.take_attendance, name='take-attendance'),
    path('attendance/view/<int:subject_id>', views.view_attendance, name='view-attendance'),
]
