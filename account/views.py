from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib import messages




# Create your views here.
def user_registration(request):
    context = {}
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            redirect("account:login")
        else:
            context['form']=form
    else:
        form = RegisterForm()
        context['form']=form
    return render(request, 'signup.html', context)


def user_login(request):
    context = {}
    if request.method == "POST":
        form = LoginForm(request.POST)
        print("ok")
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            print(email)
            user = authenticate(email=email, password=password)
            if user is not None:
                login(request, user)
                print(request, f"You are now logged in as {email}.")
                return redirect("account:home")
            else:
                print(request,"Invalid username or password.")

        else:
            context['form']=form

            messages.error(request,"Invalid username or password.")
    else:
        form = LoginForm()
        context['form']=form
    return render(request, 'signup.html', context)


def home(request):
    return render(request, 'index.html')