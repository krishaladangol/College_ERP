from django.urls import path
from . import views
urlpatterns = [
    #Student urls
    path('',views.add_student,name="add_student"),
    path('view_student',views.view_student,name='view_student'),
    path('edit_student/<int:student_id>',views.edit_student,name="edit_student"),
    path('delete_student/<int:student_id>',views.delete_student,name="delete_student"),

    #teacher urls
    path('teacher_add',views.teacher_add,name="teacher_add"),
    path('view_teacher',views.view_teacher,name="view_teacher"),
    path('edit_teacher/<int:teacher_id>',views.edit_teacher,name="edit_teacher"),
    path('delete_teacher/<int:teacher_id>',views.delete_teacher,name="delete_teacher")
]
