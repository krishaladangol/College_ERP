from django.urls import path
from . import views
urlpatterns = [
    path('',views.add_student,name="add_student"),
    # path('attendance/<int:teacher_id>',views.attendance,name='attendance'),
    # path('attendance',views.attendance,name='attendance'),

    path('teacher_add',views.teacher_add,name="teacher_add"),
    path('view_teacher',views.view_teacher,name="view_teacher"),
    path('edit_teacher/<int:teacher_id>',views.edit_teacher,name="edit_teacher"),
    path('delete_teacher/<int:teacher_id>',views.delete_teacher,name="delete_teacher")
]
