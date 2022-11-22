from django.shortcuts import render
from .forms import SignUpForm

def student_sign_up(request):
    form = SignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})
