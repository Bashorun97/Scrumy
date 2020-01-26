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

    dictionary = {'error': 'A record with that goal id does not exist'}
    try:
        goalname = ScrumyGoals.objects.get(goal_id = '%s' % goal_id)
    except Exception as e:
        return render(request, 'bashorunemmascrumy/exception.html', dictionary)
    else:
        return HttpResponse(goalname.goal_id)
    '''
    name = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(f'{name}')
    '''

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

def home1(request):
   '''
    all_users = User.objects.all()
    weeklygoal = GoalStatus.objects.get(status_name= "Weekly Goal")
    goalweekly = weeklygoal.scrumygoals_set.all()
    dailygoal = GoalStatus.objects.get(status_name= "Daily Goal")
    goaldaily = dailygoal.scrumygoals_set.all()
    verifygoal = GoalStatus.objects.get(status_name= "Verify Goal")
    goalverify = verifygoal.scrumygoals_set.all()
    donegoal = GoalStatus.objects.get(status_name= "Done Goal")
    goaldone = donegoal.scrumygoals_set.all()

    dictionary = {'user':all_users, 'weekly':goalweekly, 'daily':goaldaily, 'verify':goalverify, 'done':donegoal}
    return render(request, 'bashorunemmascrumy/home.html', dictionary)
    '''
   goal_name = ScrumyGoals.objects.get(goal_name="Learn Django")

   dictionary = {'goal_name': goal_name.goal_name, 'goal_id':goal_name.goal_id, 'user':goal_name.user}
   return render(request, 'bashorunemmascrumy/home.html', dictionary)
   
