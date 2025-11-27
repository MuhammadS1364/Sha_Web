from django.urls import path
from . import views



urlpatterns = [
    path('register-programe/', views.Add_Programes, name="Add_Programes"),
    path('register-candidate/', views.Register_StudentToPrograme, name="Register_StudentToPrograme"),
    path('select-programe-upload/', views.Select_Programe_ForResult, name="Select_Programe_ForResult"),
    path('result-upload/<str:programe_id>/', views.Upload_Result, name="Upload_Result"),
    path('dir-result-upload/<int:programe_id>/', views.Direct_To_Upload_Result, name="Direct_To_Upload_Result"),
    path('close-registration/<int:programe_id>/', views.Registrations_On_Off, name="Registrations_On_Off"),
    path('result-view/<int:programe_id>/', views.View_Programe_Results, name="View_Programe_Results"),
]