from django import forms
from django.test import TestCase
from lessons.forms import StudentSignUpForm, LogInForm
from lessons.models import User

class SignupFormTestCase:
    # If it works for student signup it will work for adult cause both classes have the same attributes
    def setUp(self):
        self.form_input = {'first_name': 'John', 'last_name': 'Doe', 'username': 'jd123', 'email': 'jd123@gmail.com'}

    def test_valid_sign_up(self):
        form = StudentSignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_form_has_required_fields(self):
        form = StudentSignUpForm()
        self.assertIn('first_name', form.fields)
        self.assertIn('last_name', form.fields)
        self.assertIn('username', form.fields)
        self.assertIn('email', form.fields)
        email_field = form.fields['email']
        self.assertTrue(isinstance(email_field, forms.EmailField))
        self.assertIn('new_password', form.fields)
        new_password_widget = form.fields['new_password'].widget
        self.assertTrue(isinstance(new_password_widget, forms.PasswordInput))
        self.assertIn('password_confirmation', form.fields)
        password_confirmation_widget = form.fields['password_confirmation'].widget
        self.assertTrue(isinstance(password_confirmation_widget, forms.PasswordInput))

    def test_model_validation(self):
        self.form_input['username'] = 'badusername'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_passwords_identical(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_correct_save(self):
        form = StudentSignUpForm(data=self.form_input)
        before = User.objects.count()
        form.save()
        after = User.objects.count()
        self.assertTrue(after == before+1)
        user = User.objects.get(username='jd123')
        self.assertEqual(user.first_name, 'John')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'jd123@gmail.com')



class LoginFormTestCase:
    def setUp(self):
        self.form_input = {'Username':'jd123', 'password':'password0'}