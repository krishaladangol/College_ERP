from django.urls import path
from . import views
urlpatterns = [
    path('teacherlogin',views.login,name="Login"),
    path('dashboard/<str:teacher_id>',views.teacher_dashboard,name="dashboard"),
    path('profile/<str:teacher_id>',views.profile,name="profile"),
    path('add_assignment',views.add_assignment,name="add_assignment"),
    path('view_assignment',views.view_assignment,name='view_assignment'),
]
