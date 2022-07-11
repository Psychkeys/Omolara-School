from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . forms import UserRegisterForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('mail_letter')
    else:
        form = UserRegisterForm()
    return render (request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    return render(request, 'users/profile.html')



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'You have successfully logged as {username}!')
            return redirect('mail_letter')
        else:
            messages.success(request, ('There Was An Error Logging In, Please Try Again'))
            return redirect('users/login')

    else:
        return render(request, 'users/login.html', {})

