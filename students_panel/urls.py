from django.urls import path
from . import views



urlpatterns = [
    path('addOutReach/', views.add_OutReach, name="add_OutReach"),
    path('outReach-view/', views.OutReach_List, name="OutReach_List"),
    path('achieve-ment-view/', views.add_AchieveMents, name="add_AchieveMents"),
]