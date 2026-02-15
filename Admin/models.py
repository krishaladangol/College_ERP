from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True,blank=True)
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Grade=models.CharField(max_length=100)
    course=models.CharField(max_length=100,default="BIT")
    # username=models.CharField(max_length=100,default="student")
    # password=models.CharField(max_length=100,default="password")

    def __str__(self):
        return f"{self.Firstname}-{self.Lastname}"

class Teacher(models.Model):
    # TeacherID = models.CharField(max_length=100,primary_key=True)    
    # Teachername=models.CharField(max_length=100)
    # department=models.CharField(max_length=100,default="IT")
    # username=models.CharField(max_length=100)
    # password=models.CharField(max_length=100)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    TeacherID = models.CharField(max_length=100, unique=True)
    Teachername = models.CharField(max_length=100)
    department = models.CharField(max_length=100, default="IT")
    def __str__(self):
        return self.Teachername

    
class Subject(models.Model):
    Teachername=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    assigned_class=models.CharField(max_length=100,default="AI")
    subject_name=models.CharField(max_length=100,default="Python")

    def __str__(self):
        return f"{self.subject_name}"
    
class Attendance(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    date = models.DateField()
    
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
        ('Leave', 'Leave'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    remarks = models.CharField(max_length=200, blank=True, null=True)

    

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.date}"
    

class Assignment(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    assigned_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    total_marks = models.IntegerField()

    file = models.FileField(upload_to='assignments/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    submitted_file = models.FileField(upload_to="submissions/")
    submitted_at = models.DateTimeField(auto_now_add=True)

    marks_obtained = models.IntegerField(null=True, blank=True)
    feedback = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.student} {self.assignment.title}"


