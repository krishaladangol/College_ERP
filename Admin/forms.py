from django import forms
class Student_form(forms.Form):
    Firstname=forms.CharField(max_length=100)
    Lastname=forms.CharField(max_length=100)
    Grade=forms.CharField(max_length=100)
    Course=forms.CharField(max_length=100)
class attendance_add(forms.Form):
    CHOICES=(
        ('Present','P'),
        ('Absent','A')
    )
    attendance=forms.CharField(max_length=50)


class Teacher_add(forms.Form):
    Teachername=forms.CharField(max_length=100)
    Subject=forms.CharField(max_length=100)
    Assignedclass=forms.IntegerField()