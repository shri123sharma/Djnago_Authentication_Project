from pipes import Template
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.views import View
from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as dj_login 
from django.contrib.auth import logout as dj_logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):
    if request.method=='POST':
        form=NewUserForm(data=request.POST)
        print(request.POST)
        print(form.is_valid())
        if form.is_valid():
            form.save()
            print('Yes')
            messages.success(request,'registration sucessful')
            return redirect('signin')
        else:
            print(form.errors)
        return render(request,'signup.html',{'form':form})
    
    else:
        form= NewUserForm()
        return render(request,'signup.html',{'form':form})

def login(request):
    if request.method=='POST':
        form=AuthenticationForm(data=request.POST)
        print(request.POST)

        # import pdb;pdb.set_trace()
        if form.is_valid():
            print(form.is_valid())
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request,username=username,password=password)
            print(form.cleaned_data)
            if user is not None:
                dj_login(request, user)
                return redirect('signout')
            else:
                messages.error(request,'Invalid username and password')
        else:
            return render(request,'signin.html',{'form':form})
        

    else:
        form=AuthenticationForm()
        return render(request,'signin.html',{'form':form})

def logout(request):
    dj_logout(request)
    return redirect('home')

def post_view(request):
    ps=Posts.objects.all()
    u1=request.user

    context={
        'ps':ps,
        'u1':u1
    }

    return render(request,'main.html',context)

def like_post(request):
    user=request.user
    if request.method=='POST':
        post_id=request.POST.get('post_id')
        post_obj=Posts.objects.filter(id=post_id).first()

        if user in post_obj.liked.all():
            post_obj.liked.remove(user)
        else:
            post_obj.liked.add(user)

        like,created=Like.objects.get_or_create(user=user,post_id=post_id)
        if not created:
            if like.value=='Like':
                like.value='UnLike'

            else:
                like.value=='Like'

        like.save()
    return redirect('postview')

def my_profile(request):
    profile=Profile.objects.get_or_create(user=request.user)

    context={'profile':profile}

    return render(request,'profile.html',context)

def search_bar(request):
    
    # import pdb;pdb.set_trace()
    if 'searchdata' in request.GET:
        search=request.GET['searchdata']    
        inform=FriendList.objects.filter(Q(first_name__icontains=search)|Q(last_name__icontains=search))
    else:
        inform=FriendList.objects.all()
    context={
        'inform':inform,
        }
    return render(request,'searchbar.html',context)
# return HttpResponse('thanks')



