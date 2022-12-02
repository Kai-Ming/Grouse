from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import *

def student_sign_up(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_page")
    else:
        form = StudentSignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})

@login_required
def teacher_sign_up(request):
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_page")
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_sign_up.html', {'form': form})

def adult_sign_up(request):
    if request.method == "POST":
        form = AdultSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("user_page")
    else:
        form = AdultSignUpForm()
    return render(request, 'adult_sign_up.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = LogInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.POST.get('next') or 'user_page'
                return redirect(redirect_url)

    form = LogInForm()
    next = request.GET.get('next') or ''
    return render(request, 'log_in.html', {'form': form, 'next': next})

def log_out(request):
    logout(request)
    return redirect('log_in')

def user_page(request):
    return render(request, 'user_page.html')
