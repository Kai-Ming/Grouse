from django.shortcuts import render
from .forms import SignUpForm
from .forms import LogInForm

def student_sign_up(request):
    form = SignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})

def log_in(request):
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})
