from django.shortcuts import render,redirect
from .forms import StudentRegisterForm,LoginForm
# from .models import Student
from Admin.models import Teacher,Student
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

# def Registration(request):
#     if request.method=="POST":
#         form=StudentRegisterForm(request.POST)
#         if form.is_valid():
#             username=form.cleaned_data['Username']
#             roll_number=form.cleaned_data['Roll_Number']
#             if User.objects.filter(username=username).exists():
#                 messages.error(request,"Username already exists.")
#                 return redirect('account:Register')

#             if Student.objects.filter(roll_number=roll_number).exists():
#                 messages.error(request, "Roll number already exists!")
#                 return redirect('account:Register')

#             user = User.objects.create_user(
#                 username=username,
#                 email=form.cleaned_data['Email'],
#                 first_name=form.cleaned_data['Firstname'],
#                 last_name=form.cleaned_data['Lastname'],
#                 password=form.cleaned_data['Password']  
#             )
#             Student.objects.create(
#             user=user,
#             roll_number=roll_number,
#             grade=form.cleaned_data['Grade'],
#             course=form.cleaned_data['Course'],
#             birthdate=form.cleaned_data['Birthdate'],
#             gender=form.cleaned_data['Gender'],
#             role=form.cleaned_data['Role'],
#             password=form.cleaned_data['Password'],
#             phone_number=form.cleaned_data['Phone_Number']

#             )
#             # return redirect("Login")
#         else:
#             return redirect("account:Register")
#     else:
#         form=StudentRegisterForm()
#     return render(request,"Register.html",{'forms':form})

def Login(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data["username"]
            password=form.cleaned_data["password"]
         
            user=authenticate(request,username=username,password=password)
            if user is not None:
                login(request,user)
                if user.is_staff:
                    return redirect('admin-dashboard')
                
                if Teacher.objects.filter(user=user).exists():
                    return redirect('teacher-dashboard')
                
            
                if Student.objects.filter(user=user).exists():
                    return redirect('student-dashboard')
                return redirect('/')
                
            else:
                messages.error(request,"Username or Password Incorrect")
    else:
        form=LoginForm()        
    return render(request,"Login.html",{'form':form})

def loggingout(request):
    logout(request)
    return redirect('account:Login')
    

def Home(request):
    return render(request,"Home_page.html")