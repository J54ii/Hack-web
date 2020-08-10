from django.urls import path
from . import views
from django.contrib.auth.views import auth_login , auth_logout #4:57

urlpatterns =[
#    path('acc/' , views.home2 , name='home2'),
    path('login0/' , views.home2 , name='login0'),

]