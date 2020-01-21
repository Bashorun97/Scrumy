from django.contrib import admin

# Register your models here.
from .models import GoalStatus, ScrumyGoals, ScrumyHistory

admin.site.register(GoalStatus)
admin.site.register(ScrumyGoals)
admin.site.register(ScrumyHistory)
