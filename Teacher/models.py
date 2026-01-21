from django.db import models
from django.contrib.auth.models import User
from Admin.models import *
# Create your models here.

class Attendance(models.Model):
    teacher=models.ForeignKey(Subject,on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)


    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"

class Assignment(models.model):
    teacher=models.ForeignKey(Subject,on_delete=models.CASCADE)
    subject_name=models.CharField(max_length=100)
    grade=models.IntegerField()

    def __str__(self):
        return f"{self.subject_name}-Grade{self.grade}"
    