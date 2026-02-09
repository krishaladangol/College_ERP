from django import forms

class StudentRegisterForm(forms.Form):
    Firstname = forms.CharField(max_length=100)
    Lastname = forms.CharField(max_length=100)
    Username = forms.CharField(max_length=100)
    Roll_Number = forms.IntegerField()
    Grade = forms.IntegerField()
    Course = forms.CharField(max_length=100)
    Birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    choice = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    Gender = forms.ChoiceField(choices=choice)

    Email = forms.EmailField(max_length=100)
    Password = forms.CharField(widget=forms.PasswordInput)
    Confirm_Password = forms.CharField(widget=forms.PasswordInput)
    Phone_Number = forms.IntegerField()
    Role = forms.CharField(max_length=100)

class LoginForm(forms.Form):
    username=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)