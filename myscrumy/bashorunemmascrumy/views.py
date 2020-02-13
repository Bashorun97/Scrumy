from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, Group, auth 
from django.contrib.auth import get_user_model, login, authenticate
from django.contrib.auth.decorators import login_required
from bashorunemmascrumy.models import *
from bashorunemmascrumy.forms import *
import random

# Create your views here.

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
            password = form.cleaned_data['password1']
            email = form.cleaned_data['email']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
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
def get_grading_parameters(request):
    return HttpResponse("This is a Scrum Application")

@login_required(login_url="bashorunemmascrumy/accounts/login")
def add_goal(request, *args, **kwargs):
    dev = User.objects.filter(groups__name__in=['Developer'])
    qa = User.objects.filter(groups__name__in=['Quality Assurance'])
    admin = User.objects.filter(groups__name__in=['Admin'])
    own = User.objects.filter(groups__name__in=['Owner'])
    if request.user in dev:
        form = DeveloprCreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = DeveloprCreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.goal_status = GoalStatus.objects.get(status_name="Weekly Goal")
                add_goal.save()
                return redirect  ("/bashorunemmascrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = DeveloprCreateGoalForm()
            return render (request, 'bashorunemmascrumy/addgoal.html', dictionary)
    
        
    elif request.user in qa:
        form = QACreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = QACreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.goal_status = GoalStatus.objects.get(status_name="Weekly Goal")
                add_goal.save()
                add_goal.save()
                return redirect  ("/bashorunemmascrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = QACreateGoalForm()
    
        return render (request, 'bashorunemmascrumy/addgoal.html', dictionary)
    elif request.user in admin:
        form = CreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = CreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.save()
                return redirect  ("/bashorunemmascrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = CreateGoalForm()
    
        return render (request, 'bashorunemmascrumy/addgoal.html', dictionary)
    elif request.user in own:
        form = CreateGoalForm()
        dictionary = {'form' : form}
        if request.method =='POST':
            form = CreateGoalForm(request.POST)
            if form.is_valid():
                add_goal = ScrumyGoals()
                add_goal = form.save(commit = False)
                add_goal.goal_id = random.randint(1000, 9999)
                add_goal.save()
                return redirect  ("/bashorunemmascrumy/home")       
            return HttpResponse("Invalid credentials provided, please fill out all fields")
        else:
            form = CreateGoalForm()
    
        return render (request, 'bashorunemmascrumy/addgoal.html', dictionary)

@login_required(login_url="bashorunemmascrumy/accounts/login")
def move_goal(request, goal_id):
    current_user = request.user
    usr_grp = request.user.groups.all()[0]
    print(usr_grp)
    goals = get_object_or_404(ScrumyGoals, goal_id=goal_id)
    if usr_grp == Group.objects.get(name='Developer') and current_user == goals.user:
        if request.method == 'POST':
            form = DeveloperChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = GoalStatus.objects.all()
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect("/bashorunemmascrumy/home")
        else:
            form = DeveloperChangeGoalForm()
        

    elif usr_grp == Group.objects.get(name='Quality Assurance') and current_user == goals.user:
        if request.method == 'POST':
            form = QAChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                # get_status = selected_status.goal_status
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/bashorunemmascrumy/home")
        else:
            form = QAChangeGoalForm()
    elif usr_grp == Group.objects.get(name='Quality Assurance') and current_user != goals.user:
        print(current_user != goals.user)
        if request.method == 'POST':
            form = QAChangeGoalForm1(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/bashorunemmascrumy/home")
        form = QAChangeGoalForm1()
    elif usr_grp == Group.objects.get(name='Owner') and current_user == goals.user:
        if request.method == 'POST':
            form = OwnerChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/bashorunemmascrumy/home")
        form = OwnerChangeGoalForm()

    elif usr_grp == Group.objects.get(name='Admin'):
        if request.method == 'POST':
            form = AdminChangeGoalForm(request.POST)
            if form.is_valid():
                selected_status = form.save(commit=False)
                selected = form.cleaned_data['goal_status']
                choice = GoalStatus.objects.get(id=int(selected))
                goals.goal_status = choice
                goals.save()
                return redirect ("/bashorunemmascrumy/home")
    else:
        return HttpResponse('You are not authorised to move this goal')
    form = AdminChangeGoalForm()
    return render(request, 'bashorunemmascrumy/movegoal.html',
                  {'form': form, 'goals': goals, 'current_user': current_user})

def signupsuccess(request):
    return render(request, 'bashorunemmascrumy/signupsuccess.html')
