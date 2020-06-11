from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.forms import ModelForm, CharField, PasswordInput, Form
from django import forms
'''
# Create your models here.

dev_grp = Group.objects.get(pk=1)
admin_grp = Group.objects.get(name ="Admin")
qa_grp = Group.objects.get(name ="Quality Assurance")
owner_grp = Group.objects.get(name ="Owner")

# === PERMISSION ===

admin_perm = Permission.objects.all()
dev_perm = Permission.objects.get(name='Can add scrumy goals')
qa_perm = Permission.objects.get(name='Can change goal status')
owner_perm = Permission.objects.get(name='Can add scrumy goals')
'''
class GoalStatus(models.Model):
    status_name = models.CharField(max_length=50)

    def __str__(self):
        return self.status_name

class ScrumyGoals(models.Model):
    goal_name = models.CharField(max_length=50)
    goal_id = models.IntegerField()
    created_by = models.CharField(max_length=50)
    moved_by = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    goal_status = models.ForeignKey(GoalStatus, on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_goal", on_delete=models.CASCADE)

    def __str__(self):
        return self.goal_name

class ScrumyHistory(models.Model):
    moved_by = models.CharField(max_length=50)
    created_by = models.CharField(max_length=50)
    moved_from = models.CharField(max_length=50)
    moved_to = models.CharField(max_length=50)
    time_of_action = models.DateField()
    goal = models.ForeignKey(ScrumyGoals, on_delete=models.CASCADE)

    def __str__(self):
        return self.created_by

class SignUpForm(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

class CreateGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']

class MoveMyGoalForm(ModelForm):
    class Meta:
        model = ScrumyGoals
        fields = ['goal_name', 'user']
