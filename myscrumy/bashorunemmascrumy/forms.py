'''
from django import forms
from django.contrib.auth.forms import UserCreationForm
from bashorunemmascrumy.models import ScrumyGoals, GoalStatus
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}))

    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']

#Change goals
class DeveloperChangeGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[0:3]])
    
    class Meta():
        model = GoalStatus
        fields = ['goal_status']

class QAChangeGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[0:4]])

    class Meta():
        model = GoalStatus
        fields = ['goal_status']

class QAChangeGoalForm1(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[2:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']

class OwnerChangeGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']

class AdminChangeGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']

# Create Goal

class DeveloperCreateGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[0:1]])

    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user']

class QACreateGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[0:1]])

    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user']

class QACreateGoalForm1(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[2:4]])

    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user']
    
class OwnerCreateGoalForm(forms.ModelForm):
    query_set = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in query_set.order_by('id')[0:1]])

    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user']





class CreateGoalForm(forms.ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user', 'goal_status']


class ChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset[:3]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']
'''