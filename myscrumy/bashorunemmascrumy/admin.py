from django.contrib import admin

# Register your models here.
from .models import ScrumyGoals, ScrumyHistory, GoalStatus

admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
admin.ste.register(GoalStatus)
