from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator


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
        unique=True, validators=[RegexValidator(
            regex=r'^\w{3,16}$',
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
