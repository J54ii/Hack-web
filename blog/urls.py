from django.urls import path 
from . import views
from django.conf.urls import url
from .views import PostCreateView
urlpatterns =[
    path('' , views.home , name='home'),
    path('newAccount/' , views.new1, name='new1'),
    path('newBack/' , views.newBack, name='newBack'),

    path('log/' , views.login, name='log1'),
    path('logBack/' , views.logBack, name='logBack'),
    #url(r'profile/(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile),

    url('profile/<slug:slug>/' , views.profileD, name='pro1'),
    path('ask/',views.ask, name='ask1'),
   # path('ask/',PostCreateView.as_view(), name='ask1'),
    path('answer',views.answer,name='ans1'),
    path('logoutBack/', views.logoutBack , name='out1')

   # re_path(r"^profile/(?P<username>)/$" , views.profile, name='pro1'),


]