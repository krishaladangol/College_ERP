from django import forms
from Admin.models import Subject,Teacher

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class AddAssignment(forms.Form):
    teacher=forms.ModelChoiceField(queryset=Teacher.objects.all())
    subject = forms.ModelChoiceField(queryset=Subject.objects.all())
    title = forms.CharField(max_length=200)
    description = forms.CharField(widget=forms.Textarea)
    assigned_date = forms.DateField()
    due_date = forms.DateField()
    total_marks = forms.IntegerField()
    file = forms.FileField()