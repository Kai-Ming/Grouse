from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.core.validators import MinValueValidator, MinLengthValidator

# Create your models here.


# A generic user class.
class User(AbstractUser):
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

class Lesson(models.Model):

    LESSON_NUMBER_CHOICES = (
        (1,"1"),
        (2,"2")    
    )
    LESSON_DURATION_CHOICES = (
        (30,"30"),
        (45,"45"),
        (60,"60")
    ) 
    PAID_TYPE_CHOICES = {
        (1, "unpaid"),
        (2, "paid"),
        (3, "partially paid"),
        (4, "overpaid")
    } 

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    number_of_lessons = models.PositiveIntegerField(choices=LESSON_NUMBER_CHOICES, default=1)
    lesson_duration = models.PositiveIntegerField(choices=LESSON_DURATION_CHOICES, default=30)
    teacher = models.CharField(max_length=100, default='', blank=True)
    price = models.FloatField(validators=[MinValueValidator(0)])
    fulfilled = models.BooleanField(default=False)
    paid_type = models.PositiveIntegerField(choices=PAID_TYPE_CHOICES, default=1)

 
