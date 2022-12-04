from django import forms
from django.test import TestCase
from lessons.forms import StudentSignUpForm, LogInForm
from lessons.models import User

class SignupFormTestCase:
    # If it works for student signup it will work for adult cause both classes have the same attributes
    def setUp(self):
        self.form_input = {'first_name': 'John', 'last_name': 'Doe', 'username': 'jd123', 'email': 'jd123@gmail.com'}

    