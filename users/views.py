from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from project.models import Project
from django.contrib import messages
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.contrib.auth.models import Group

# Create your views here.

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'post':
        form = createuserform(request.post)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Student')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + username )
            return redirect('loginPage')
    context ={'form' : form}
    return render(request,'users/register.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username , password=password)
        if user is not None:
            login(request,user)
            # return render(request,'student/home.html')
            return redirect('home')
        else:
            messages.info(request,'username OR password is incorrect')
    return render(request,'users/login.html')

def logoutUser(request):
    logout(request)
    return redirect('loginPage')
