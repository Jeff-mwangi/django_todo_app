from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import RegisterNewUser, UserUpdateForm, ProfileUpdateForm
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from users.models import Profile

def register(request):
    if request.method == 'POST':
        form = RegisterNewUser(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, 'Account created successfully')
            return redirect('login')
    else:
        form = RegisterNewUser()
    return render (request, 'users/register.html', {'form': form})

def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('home')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/update_profile.html', context)
