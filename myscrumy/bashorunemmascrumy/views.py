from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, ScrumyHistory, User, GoalStatus

# Create your views here.
'''
def get_grading_parameters(request):
    return HttpResponse("This is a Scrum Application")
'''
def query_filter(request):
    name = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(name)
