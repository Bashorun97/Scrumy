
from django import forms
from django.contrib.auth.forms import UserCreationForm
from bashorunemmascrumy.models import ScrumyGoals, GoalStatus
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

User = get_user_model()

class SignUpForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email    = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Emaill'}))
   
    class Meta():
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']


# changin goals
class DeveloperChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[0:3]])
    class Meta():
        model = GoalStatus
        fields = ['goal_status']


class QAChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']

class QAChangeGoalForm1(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[2:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']

class OwnerChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']


class AdminChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[:4]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']



#create goal form

class DeveloprCreateGoalForm(forms.ModelForm):
    goal_status = ScrumyGoals()
    goal_status = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in goal_status.order_by('id')[0:1]])
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user',]

class QACreateGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[0:1]])
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user', ]

class OwnerCreateGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset.order_by('id')[0:1]])
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user', ]


class CreateGoalForm(forms.ModelForm):
        class Meta:
            model = ScrumyGoals
            fields = ['goal_name', 'created_by', 'moved_by', 'owner', 'user', 'goal_status',]


class ChangeGoalForm(forms.ModelForm):
    queryset = GoalStatus.objects.all()
    goal_status = forms.ChoiceField(choices=[(choice.pk, choice) for choice in queryset[:3]])

    class Meta:
        model = GoalStatus
        fields = ['goal_status']
