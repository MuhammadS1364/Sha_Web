from django.urls import path
from . import views



urlpatterns = [
    path('register-programe/', views.Add_Programes, name="Add_Programes"),
    path('register-candidate/', views.Register_StudentToPrograme, name="Register_StudentToPrograme"),
   
]