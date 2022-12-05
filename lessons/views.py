
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.shortcuts import redirect, render
from .checks import *
from .forms import *
from .models import *

def login_prohibited(view_function):
    def modified_view_function(request):
        if request.user.is_authenticated:
            return redirect('user_page')
        else:
            return view_function(request)
    return modified_view_function

def student_sign_up(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = StudentSignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})

@user_passes_test(admin_rights_check)
def teacher_sign_up(request):
    if request.method == "POST":
        form = TeacherSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = TeacherSignUpForm()
    return render(request, 'teacher_sign_up.html', {'form': form})

def adult_sign_up(request):
    if request.method == "POST":
        form = AdultSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = AdultSignUpForm()
    return render(request, 'adult_sign_up.html', {'form': form})

@login_prohibited
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
        messages.add_message(request, messages.ERROR, "The credentials provided were invalid!")
    form = LogInForm()
    next = request.GET.get('next') or ''
    return render(request, 'log_in.html', {'form': form, 'next': next})

@login_required
def log_out(request):
    logout(request)
    return redirect('log_in')

@login_required
def user_page(request):
    curr_username = request.user.username
    curr_name = request.user.first_name + request.user.last_name
    curr_email = request.user.email

    curr_id = request.user.id

    curr_enrolled_lessons = Lesson.objects.filter(student=curr_id)
    
    """ # Continue here. Figure out how the invoice system works and continue from here
    # May or may not work -- Need to test
    invoice_list = models.Invoice.objects.extra(where=["%s LIKE invoice_no||'%%'"], params=[curr_id]) """


    context = {
        'curr_username': curr_username,
        'curr_name': curr_name,
        'curr_email': curr_email,
        'enrolled_lesson_data': curr_enrolled_lessons,
        #'invoice_list': invoice_list
    }


    return render(request, 'user_page.html')

def admin_page(request):
    curr_requests = models.Lesson.objects.filter(fulfilled="0")

    curr_records = models.Transfer.objects.filter()


    context = {
        'curr_requests': curr_requests,
        'curr_records': curr_records
    }

    return(render, 'admin_page.html')