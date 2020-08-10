from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse , HttpResponseRedirect
from django.contrib.auth import authenticate 
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .models import profile
from django.shortcuts import get_object_or_404
from .models import post , comment
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import PostCreateForm


# Create your views here

def home(request): 
    return render(request ,'blog/index.html' , {'title' : 'Home'})

def new1(request):
    return render(request , 'blog/register.html')

def login(request):
    return render(request , 'blog/login.html')

def profileD(request , username):
    return render(request , 'blog/survey.html')
    profile = profile.objects.get(username)#slug=slug)
    context = {
        'profile' : profile ,
    }
    return render(request , 'blog/survey.html')


def ask(request):
 #   post2 = post.objects.PostCreateView()
    return render(request , 'blog/application.html')
    
def answer(request):
    post1 = post.objects.get()
    com1 = comment.objects.get()
    context = {
        "post1":post1 , 
        "com1" :com1,
    
    }
    return render(request, 'blog/signup.html',context )


#from django.shortcuts import render
####123###
def get_user_profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'blog/survey.html', {"user":user})




def newBack(request): #مستخدم جديد
    try:
        user=User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.age=request.POST['age']
        user.age=request.POST['phone']
        user.save()
        messages.success(request,' شكراً لك على التسجيل  ')
        return render(request , 'blog/survey.html' , {'user':user})

    except:
        return render(request , 'blog/login3.html')


class PostCreateView(CreateView):
    model = post
    template_name = 'blog/application.html'
    field =['title' , 'text1']
    form_class = PostCreateForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def logBack(request):
    u=request.POST['username']
    p=request.POST['password']
    re=authenticate(username=u, password=p)

    if re is not None:
        print('log in')
        auth_login(request,re)
       # link='/profile/'+str(re)
        #return HttpResponseRedirect(link)
        return render(request , 'blog/survey.html')
    else:
        return render(request , 'blog/login2.html')

def logoutBack(request):
    auth_logout(request)
    print('log in')
    return render(request ,'blog/index.html' , {'title' : 'Home'})

