from django.urls import path
from . import views


urlpatterns = [
    path('',views.Home,name="Home"),
    path('register',views.Registration,name="Register"),
    path('login',views.Login,name="Login"),

]
