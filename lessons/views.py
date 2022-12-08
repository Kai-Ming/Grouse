from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ImproperlyConfigured, ObjectDoesNotExist
from django.http import HttpResponseForbidden, Http404
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.urls import reverse
from .forms import *
from .models import *
from .helpers import *
from django.utils import timezone
from datetime import timedelta
from django.db.utils import IntegrityError
from django.core.validators import ValidationError


def student_sign_up(request):
    if request.method == "POST":
        form = StudentSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("user_page")
    else:
        form = StudentSignUpForm()
    return render(request, 'student_sign_up.html', {'form': form})

@login_required
@admin_login_required
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
@admin_login_prohibited
def user_page(request):
    curr_username = request.user.username
    curr_name = request.user.first_name + request.user.last_name
    curr_email = request.user.email

    curr_id = request.user.id
    lesson_requests = Lesson.objects.filter(student=curr_id, fulfilled="0")
    lesson_bookings = Lesson.objects.filter(student=curr_id, fulfilled="1")

    # Still needs testingg.
    invoices = Invoice.objects.extra(where=["%s LIKE invoice_no||'%%'"], params=[curr_id])

    context = {
        'curr_username': curr_username,
        'curr_name': curr_name,
        'curr_email': curr_email,
        'lessons': lesson_requests,
        'bookings': lesson_bookings,
        'invoices': invoices
    }
    
    return render(request, 'user_page.html', context)


@login_required
@admin_login_required
def admin_page(request):
    curr_username = request.user.username
    curr_name = request.user.first_name + request.user.last_name
    curr_email = request.user.email

    curr_requests = Lesson.objects.filter(fulfilled="0")
    curr_records = Transfer.objects.all()

    fulfilled_lessons = Lesson.objects.filter(fulfilled="1")

    invoices = Invoice.objects.all()

    if request.method == "POST":
        if request.POST.get("accept"):
            lesson = Lesson.objects.get(pk=request.POST['accept'][0])
            lesson.fulfilled = True
            lesson.save(update_fields=["fulfilled"])
            return redirect("admin_page")

        elif request.POST.get("reject"):
            lesson = Lesson.objects.get(pk=request.POST['reject'][0])
            lesson.delete()
            return redirect("admin_page")

        elif request.POST.get("generate"):
            invoice_no = ''

            lesson = Lesson.objects.get(pk=request.POST['generate'][0])
            user_id = lesson.student_id
            student_no = f'{user_id:04}'

            due_amount = lesson.price

            if lesson.lesson_duration == 45:
                due_amount = lesson.price * 2
            elif lesson.lesson_duration == 60:
                due_amount = lesson.price * 3

            due_date = timezone.now() + timedelta(days=30)      # all invoices are due 30 day after invoice is created

            n = 0
            while True:
                try:
                    n += 1
                    invoice_no = f'{student_no}-{n:04}'

                    Invoice.objects.create(
                        invoice_no=invoice_no,
                        due_amount=due_amount,
                        due_date=due_date
                    )

                    print(f'Generated invoice: {invoice_no}')
                    break
                except IntegrityError:
                    continue

            lesson.invoice = invoice_no
            lesson.save(update_fields=['invoice'])

            return redirect('admin_page')

        elif request.POST.get('record_transfer'):
            # create a transfer here
            # update the associated lesson paid type
            return redirect('admin_page')

    context = {
        'curr_username': curr_username,
        'curr_name': curr_name,
        'curr_email': curr_email,
        'curr_requests': curr_requests,
        'curr_records': curr_records,
        'fulfilled_lessons': fulfilled_lessons,
        'invoices': invoices
    }

    return render(request, 'admin_page.html', context)


@login_required
@admin_login_prohibited
def lesson_request(request):
    if request.method == "POST":
        form = LessonRequestForm(request.POST)
        if form.is_valid():
            student = request.user
            number_of_lessons = form.cleaned_data.get('number_of_lessons')
            lesson_duration = form.cleaned_data.get('lesson_duration')
            teacher = form.cleaned_data.get('teacher')
            lesson = Lesson.objects.create(student=student, number_of_lessons=number_of_lessons, lesson_duration=lesson_duration, teacher=teacher)
            return redirect('user_page')
    else:
        form = LessonRequestForm()
    return render(request, 'lesson_request.html', {'form': form})


@login_required
@admin_login_required
def edit_lesson(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    form = LessonEditForm(request.POST or None, request.FILES or None, instance=lesson)
    if form.is_valid():
        form.save()
        return redirect('admin_page') 
    return render(request, 'edit_lesson.html', {'lesson': lesson, 'form': form})


@login_required
def edit_lesson_student(request, lesson_id):
    lesson = Lesson.objects.get(pk=lesson_id)
    form = LessonRequestForm(request.POST or None, request.FILES or None, instance=lesson)
    if (lesson != None):
        if (lesson.student == request.user and lesson.fulfilled == 0):
            if form.is_valid():
                form.save()
                return redirect('user_page') 
            return render(request, 'edit_lesson_student.html', {'lesson': lesson, 'form': form})
        else:
            return redirect('user_page')
    else:
        return redirect('user_page')


@login_required
@admin_login_required
def record_transfer(request):
    if request.method == 'POST':
        form = RecordTransferForm(request.POST)

        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            invoice_number = form.cleaned_data.get('invoice_number')
            date = form.cleaned_data.get('date')

            try:
                Transfer.objects.create(invoice_number=invoice_number, amount=amount, date=date)
                print(f'Recorded transfer for {invoice_number}')
            except ValidationError as err:
                print(f'Transfer couldn\'t be recorded: {err}')

            return redirect('admin_page')
    else:
        form = RecordTransferForm()

    return render(request, 'record_transfer.html', {'form': form})
