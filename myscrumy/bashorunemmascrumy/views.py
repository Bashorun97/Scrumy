from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group, auth 
from django.contrib.auth.decorators import login_required
from bashorunemmascrumy.models import *
from django.views.generic import TemplateView
import random

# Create your views here.

@login_required(login_url="/bashorunemmascrumy/accounts/login")
def get_grading_parameters(request):
    return HttpResponse("This is a Scrum Application")

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
    

#def query_filter(request):
#    name = ScrumyGoals.objects.filter(goal_name="Learn Django")
#    return HttpResponse(name)

def home1(request):
   goal_name = ScrumyGoals.objects.get(goal_name="Learn Django")

   dictionary = {'goal_name': goal_name.goal_name, 'goal_id':goal_name.goal_id, 'user':goal_name.user}
   return render(request, 'bashorunemmascrumy/home.html', dictionary)


@login_required(login_url="/bashorunemmascrumy/accounts/login")
def home(request):
    goal = ScrumyGoals.objects.get(goal_name="Keep Learning Django")

    all_users = User.objects.all()
    weekly_goals = GoalStatus.objects.get(status_name="Weekly Goal")
    goals_weekly = weekly_goals.scrumygoals_set.all()

    daily_goals = GoalStatus.objects.get(status_name="Daily Goal")
    goals_daily = daily_goals.scrumygoals_set.all()

    verify_goals = GoalStatus.objects.get(status_name="Verify Goal")
    goals_verify = verify_goals.scrumygoals_set.all()

    done_goals = GoalStatus.objects.get(status_name="Done Goal")
    goals_done = done_goals.scrumygoals_set.all()

    
    dictionary = {'users': all_users, 'weekly': goals_weekly, 'daily': goals_daily, 'verify': goals_verify, 'done': goals_done}
    return render(request, "bashorunemmascrumy/home.html", dictionary)


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
        else:
            return redirect('login')
    else:
        return redirect ('login')
    return render (request,'login.html')


def sign_up(request):
    #dictionary = {'error':'invalid login credentials'}
    #return render(request, 'registration/signup.html', dictionary)
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user (username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print('signup successful')
            new_user = User.objects.get(username=username)
            group = Group.objects.get(name='Developer')
            group.user_set.add(new_user)

            #success_dic = {'success':'Congrats! SignUp successful'}
            return HttpResponseRedirect('signupsuccess')
    else:
        form
    return render(request, 'registration/signup.html', {'form':form})

@login_required(login_url="/bashorunemmascrumy/accounts/login")
def add_goal(request):
    form = CreateGoalForm()
    if request.method == 'POST':
        form = CreateGoalForm(request.POST)
        track = list(range(1000, 9999))
        random_number = random.sample(track, k=1)
        weeklygoal = GoalStatus.objects.get(status_name="Weekly Goal")

        for i in random_number:
            value = i
        if form.is_valid():
            username = form.cleaned_data['user']
            goal_name = form.cleaned_data['goal_name']
            user = User.objects.get(username=username)

            add_goal = form.save(commit=False)
            add_goal.goal_id = value
            add_goal.created_by = user.username
            add_goal.moved_by = user.username
            add_goal.owner = user.username
            add_goal.goal_status = weeklygoal
            add_goal.save()
            return HttpResponseRedirect('home')

    context = {'create_goal': form }

    return render(request, 'bashorunemmascrumy/addgoal.html', context)

def signupsuccess(request):
    return render(request, 'bashorunemmascrumy/signupsuccess.html')
