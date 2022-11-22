from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm, UpdateForm

from .models import CustomUser


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context)
    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'register.html', context)
    return render(request, 'register.html', {})


def login_user(request):
    if request.method == 'GET':
        form = LoginForm()
        context = {'form': form}
        return render(request, 'login.html', context)
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['username'])
            print(cd['password'])
            user = CustomUser.objects.get(username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                return redirect('polls:index')
            else:
                messages.error(request, 'Bad login')
                context = {'form': form}
                return render(request, 'login.html', context)
        else:
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'login.html', context)
    return render(request, 'login.html', {})


@login_required
def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'profile.html', {})


@login_required
def delete_user(request):
    print(request.user.get_username())
    CustomUser.objects.filter(username=request.user.get_username()).delete()
    return redirect('register')


def update_user(request):
    if request.method == 'GET':
        form = UpdateForm()
        context = {'form': form}
        return render(request, 'update.html', context)
    if request.method == 'POST':
        # form = UpdateForm(request.POST, request.user, request.FILES)
        form = UpdateForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
        else:
            print('Form is not valid')
            messages.error(request, 'Error Processing Your Request')
            context = {'form': form}
            return render(request, 'update.html', context)
    return render(request, 'update.html', {})
