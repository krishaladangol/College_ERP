from django.urls import path
from . import views
urlpatterns = [
    path('teacherlogin',views.login,name="Login"),
    path('dashboard/<str:teacher_id>',views.teacher_dashboard,name="dashboard"),
    path('profile/<str:teacher_id>',views.profile,name="profile"),

]
