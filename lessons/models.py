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

class LessonRequest(models.Model):

    LESSON_NUMBER_CHOICES = (
        (1,"1"),
        (2,"2")    
    )
    LESSON_DURATION_CHOICES = (
        (30,"30"),
        (45,"45"),
        (60,"60")
    )    

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    number_of_lessons = models.PositiveIntegerField(choices=LESSON_NUMBER_CHOICES, default=1)
    lesson_duration = models.PositiveIntegerField(choices=LESSON_DURATION_CHOICES, default=30)
    teacher = models.CharField(max_length=100, blank=True)

class LessonBooking(models.Model):

    LESSON_NUMBER_CHOICES = (
        (1,"1"),
        (2,"2")   
    )
    LESSON_DURATION_CHOICES = (
        (30,"30"),
        (45,"45"),
        (60,"60")
    )  

    student = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    number_of_lessons = models.PositiveIntegerField(choices=LESSON_NUMBER_CHOICES, default=1)
    lesson_duration = models.PositiveIntegerField(choices=LESSON_DURATION_CHOICES, default=30)
    teacher = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    price = models.FloatField(validators=[MinValueValidator(0)])
 
