from django.urls import path
from . import views



urlpatterns = [
    path('addOutReach/', views.add_OutReach, name="add_OutReach"),
    path('outReach-view/', views.OutReach_List, name="OutReach_List"),
]