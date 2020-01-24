from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
       # path('', views.get_grading_parameters),
        path('', views.query_filter),
        path('<int:goal_id>/move_goal', views.move_goal, name="move_goal"),
]
