from django.shortcuts import render
from django.http import HttpResponse
from .models import ScrumyGoals, ScrumyHistory, GoalStatus
from django.contrib.auth.models import User
import random

# Create your views here.
'''
def get_grading_parameters(request):
    return HttpResponse("This is a Scrum Application")
'''
def query_filter(request):
    name = ScrumyGoals.objects.filter(goal_name="Learn Django")
    return HttpResponse(name)


def move_goal(request, goal_id):
    name = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(f'{name}')

def add_goal(request):
    goal_status= GoalStatus.objects.get(status_name="Weekly Goal")
    user = User.objects.get(username="louis")

    for i in random.sample(list(range(1000, 9999)), k=1):
        rand_id = i

    name = ScrumyGoals.objects.create(goal_name="Keep Learning Django", goal_id=rand_id, created_by="Louis", moved_by="Louis", owner="Louis", goal_status=goal_status, user=user)

    query = ScrumyGoals.objects.all()
    context = ",".join([q.goal_name for q in query])
    return HttpResponse(context)

def home(request):
    goal = ScrumyGoals.objects.get(goal_name="Keep Learning Django")
    return HttpResponse(goal)
