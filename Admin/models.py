from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname=models.CharField(max_length=100)
    Lastname=models.CharField(max_length=100)
    Grade=models.CharField(max_length=100)
    course=models.CharField(max_length=100,default="BIT")

    def __str__(self):
        return f"{self.Firstname}-{self.Lastname}"

class Teacher(models.Model):
    TeacherID = models.CharField(max_length=100,primary_key=True)    
    Teachername=models.CharField(max_length=100)

    department=models.CharField(max_length=100,default="IT")
   
    def __str__(self):
        return self.Teachername

    
class Subject(models.Model):
    Teachername=models.CharField(max_length=100)
    teacher=models.ForeignKey(Teacher,on_delete=models.CASCADE,null=True)
    assigned_class=models.CharField(max_length=100,default="AI")
    subject_name=models.CharField(max_length=100,default="Python")

    def __str__(self):
        return f"{self.Teachername}"