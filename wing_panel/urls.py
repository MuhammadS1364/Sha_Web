from django.urls import path
from . import views



urlpatterns = [
    path('register-programe/', views.Add_Programes, name="Add_Programes"),
    path('register-candidate/', views.Register_StudentToPrograme, name="Register_StudentToPrograme"),
    path('select-programe-upload/', views.Select_Programe_ForResult, name="Select_Programe_ForResult"),
    path('result-upload/<int:programe_id>', views.Upload_Result, name="Upload_Result"),
]