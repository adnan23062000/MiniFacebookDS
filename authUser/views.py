from django.shortcuts import render, redirect
from authUser.forms import studentForm
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect

# Create your views here.

def registerStudent(request):
    registered=False
    if request.method=='POST':
        var_studentForm=studentForm(request.POST)
        if var_studentForm.is_valid():
            studentprimary=var_studentForm.save()
            studentprimary.set_password(studentprimary.password)
            studentprimary.save()
            registered=True
    else:
        var_studentForm=studentForm()
    return render(request,'authUser/registerStudent.html',{'var_studentForm':var_studentForm, 'registered':registered})


def userLogin(request):
    invalidlogin=False
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:
            invalidlogin=False
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect('/newsfeed')
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin=True
            return render(request,'authUser/login.html',{'invalidlogin':invalidlogin})
    else:
        invalidlogin=False
        return render(request,'authUser/login.html',{'invalidlogin':invalidlogin})


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('userLogin'))
