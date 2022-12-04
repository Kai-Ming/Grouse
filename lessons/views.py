from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout

from .forms import *
from .models import *

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
                return redirect('user_page')

    form = LogInForm()
    return render(request, 'log_in.html', {'form': form})

def log_out(request):
    logout(request)
    return redirect('user_page')

def user_page(request):
    curr_username = request.user.username()
    curr_name = request.get_full_name()
    curr_email = request.user.email

    curr_id = request.user.id

    curr_enrolled_lessons = models.Lesson.objects.filter(student_id=curr_id)
    
    # Continue here. Figure out how the invoice system works and continue from here
    # May or may not work -- Need to test
    invoice_list = models.Invoice.objects.extra(where=["%s LIKE invoice_no||'%%'"], params=[curr_id])


    context = {
        'curr_username': curr_username,
        'curr_name': curr_name,
        'curr_email': curr_email,
        'enrolled_lesson_data': curr_enrolled_lessons,
        'invoice_list': invoice_list
    }


    return render(request, 'user_page.html')

def admin_page(request):
    curr_requests = 

    curr_records = models.Transfer.objects.filter()


    context = {
        'curr_requests': curr_requests,
        'curr_records': curr_records
    }

    return(render, 'admin_page.html')