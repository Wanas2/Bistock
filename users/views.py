from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.views.generic import ListView

from .forms import LoginForm, AddUserForm, ModifyUserForm
from .models import User


# import the logging library
# import logging

# Get an instance of a logger
# logger = logging.getLogger(__name__)


# Auth views
def login_page(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            username = forms.cleaned_data['username']
            password = forms.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    context = {'form': forms}
    return render(request, 'users/login.html', context)


def logout_page(request):
    logout(request)
    return redirect('login')


# Users views

@login_required(login_url='login')
def create_user(request):
    forms = AddUserForm()
    if request.method == 'POST':
        forms = AddUserForm(request.POST)
        if forms.is_valid():
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            username = forms.cleaned_data["username"]
            password = forms.cleaned_data['password']
            tel = forms.cleaned_data['tel']
            is_admin = forms.cleaned_data['is_admin']
            User.objects.create(
                first_name=first_name,
                last_name=last_name,
                address=address,
                email=email,
                username=username,
                password=make_password(password),
                tel=tel,
                is_admin=is_admin
            )
            return redirect('user-list')
    context = {
        'form': forms
    }
    return render(request, 'users/create_user.html', context)


@login_required(login_url='login')
def modify_user(request, user_id):
    u = User.objects.filter(pk=user_id).first()
    forms = ModifyUserForm(instance=u)
    if request.method == 'POST':
        forms = ModifyUserForm(request.POST, instance=request.user)
        if forms.is_valid():
            first_name = forms.cleaned_data['first_name']
            last_name = forms.cleaned_data['last_name']
            address = forms.cleaned_data['address']
            email = forms.cleaned_data['email']
            password = forms.cleaned_data['password']
            tel = forms.cleaned_data['tel']
            is_admin = forms.cleaned_data['is_admin']
            User.objects.filter(pk=user_id).update(
                first_name=first_name,
                last_name=last_name,
                address=address,
                email=email,
                password=make_password(password),
                tel=tel,
                is_admin=is_admin
            )
            return redirect('user-list')
    context = {
        'form': forms
    }
    return render(request, 'users/modify_user.html', context)


@login_required(login_url='login')
def delete_user(request, user_id):
    try:
        User.objects.filter(id=user_id).delete()
        messages.success(request, "delete user successfully")
    except:
        messages.error(request, "delete user failed!!!")
    return render(request, 'users/user_list.html')

class UserListView(ListView):
    model = User
    template_name = 'users/user_list.html'
    context_object_name = 'users'


@login_required(login_url="login")
def myprofil_page(request):
    return render(request, 'users/myprofil.html')