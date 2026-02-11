from django import forms
class Student_form(forms.Form):
    Firstname=forms.CharField(max_length=100)
    Lastname=forms.CharField(max_length=100)
    Grade=forms.CharField(max_length=100)
    Course=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)


class attendance_add(forms.Form):
    CHOICES=(
        ('Present','P'),
        ('Absent','A')
    )
    attendance=forms.CharField(max_length=50)


class Teacher_add(forms.Form):
    Teacherid=forms.CharField(max_length=100)
    Teachername=forms.CharField(max_length=100)
    Subject_name=forms.CharField(max_length=100)
    Assignedclass=forms.CharField(max_length=100)
    department=forms.CharField(max_length=100)
    username=forms.CharField(max_length=100)
    password=forms.CharField(max_length=100)