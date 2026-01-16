from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Grade=models.IntegerField()

    def __str__(self):
        return f"{self.Firstname}-{self.Lastname}"
    
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"
    
class Subject(models.Model):
    Teachername=models.CharField(max_length=100)
    subject=models.CharField(max_length=100)
    assigned_class=models.IntegerField()

    def __str__(self):
        return f"{self.Teachername} {self.subject}"