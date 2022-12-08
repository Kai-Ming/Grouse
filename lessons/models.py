from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator
from django.utils import timezone


class User(AbstractUser):
    """A generic user class."""

    # Add user types as necessary.
    USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'adult'),
      (3, 'teacher'),
      (4, 'admin'),
      (5, 'superadmin'),
    )

    # Define attributes.
    # All valid users must have a user type, username, first name, last name, and an email.
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, default=5)
    username = models.CharField(
        max_length=16,
        unique=True,
        validators=[RegexValidator(
            regex=r'^\w{3,}$',
            message='Username must consist of three to sixteen alphanumericals'
        )]
    )
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True, blank=False)


class Student(User):
    """A student of the music school."""

    # A student has a unique student number used for identification.
    student_no = models.PositiveIntegerField(unique=True, blank=False, primary_key=True)

    # extend the Student model as necessary


class Lesson(models.Model):
    """The model of a lesson that can be requested and fulfilled"""
    
    LESSON_NUMBER_CHOICES = (
        (1,"1"),
        (2,"2")    
    )
    LESSON_DURATION_CHOICES = (
        (30,"30"),
        (45,"45"),
        (60,"60")
    ) 
    PAID_TYPE_CHOICES = (
        (1, "Unpaid"),
        (2, "Paid"),
        (3, "Partially paid"),
        (4, "Overpaid")
    )

    BOOL_CHOICES = (
        (True, 'Accept'), 
        (False, 'Reject')
        )

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField(auto_now=False, default=timezone.now)
    number_of_lessons = models.PositiveIntegerField(choices=LESSON_NUMBER_CHOICES, default=1)
    lesson_duration = models.PositiveIntegerField(choices=LESSON_DURATION_CHOICES, default=30)
    teacher = models.CharField(max_length=100, default='', blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)], default=0)
    fulfilled = models.BooleanField(choices=BOOL_CHOICES, default=False)
    paid_type = models.PositiveIntegerField(choices=PAID_TYPE_CHOICES, default=1)
    invoice = models.CharField(max_length=25, blank=False, default='No associated invoice.')


class Invoice(models.Model):
    """An invoice for a lesson."""

    invoice_no = models.CharField(
        max_length=50,
        blank=False,
        primary_key=True,
        validators=[RegexValidator(
            regex=r'\w[0-9]+-[0-9]+$',
            message='Invoice number must only contain numbers and a dash'
        )]
    )
    due_amount = models.DecimalField(blank=False, max_digits=6, decimal_places=2)
    due_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Transfer(models.Model):
    """A transfer made by the student to the music school's bank account."""

    invoice_number = models.CharField(default='0-0', max_length=50)
    amount = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateTimeField(default=timezone.now)
