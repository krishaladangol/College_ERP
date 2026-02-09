from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    roll_number = models.IntegerField(unique=True)
    grade = models.IntegerField()
    course = models.CharField(max_length=100)
    birthdate = models.DateField()

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    phone_number = models.CharField(max_length=15)
    
    password=models.CharField(max_length=100,default="12345678")

    role = models.CharField(max_length=50, default="Student")

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"