from django.shortcuts import redirect,render
from .forms import StudentSignUpForm
from .forms import LogInForm

def student_sign_up(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = StudentSignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})

def log_in(request):
    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def user_page(request):
    return render(request, 'user_page.html')
