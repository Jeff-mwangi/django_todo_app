from django.shortcuts import render,redirect
from django.contrib import messages
from users.forms import RegisterNewUser

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
