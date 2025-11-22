from django.urls import path
from . import views



urlpatterns = [
    path('register-programe/', views.Add_Programes, name="Add_Programes"),
    path('register-candidate/', views.Register_StudentToPrograme, name="Register_StudentToPrograme"),
    path('result-upload/', views.Upload_Result, name="Upload_Result"),
    path('select-programe-upload/', views.Select_Programe_ForResult, name="Select_Programe_ForResult"),
   
]