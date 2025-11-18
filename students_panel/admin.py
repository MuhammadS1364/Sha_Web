from django.contrib import admin

# Register your models here.
from .models import *
from .forms import *


admin.site.register(OutReach_Model)
admin.site.register(Achievements_Model)