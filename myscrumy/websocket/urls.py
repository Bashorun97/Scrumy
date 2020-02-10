from django.urls import path, include
from . import views

urlpatterns = [
    path('test/', views.test, name='test'),
    path('disconnect/', views.disconnect, name='disconnect'),
    path('connect/', views.connect, name='connect'),
    path('send_message/', views.send_message, name='sendmessage'),
    ]
