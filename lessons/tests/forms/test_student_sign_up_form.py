"""Unit tests of the sign up form."""
from django.contrib.auth.hashers import check_password
from django import forms
from django.test import TestCase
from lessons.forms import StudentSignUpForm
from lessons.models import User

class SignUpFormTestCase(TestCase):
    """Unit tests of the sign up form."""


    #Set up an examplery input to use for the tests
    def setUp(self):
        self.form_input = {
            'first_name': 'Jane',
            'last_name': 'Doe',
            'username': 'janedoe',
            'email': 'janedoe@example.org',
            'new_password': 'Password123',
            'password_confirmation': 'Password123'
        }


    # Test if the form accepts valid input
    def test_valid_sign_up_form(self):
        form = StudentSignUpForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Test the form having the required fields inside it
    def test_form_has_necessary_fields(self):
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


    # Test the form using model validation
    def test_form_uses_model_validation(self):
        self.form_input['username'] = 'A'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the form not accepting a password field with no uppercase characters in it
    def test_password_must_contain_uppercase_character(self):
        self.form_input['new_password'] = 'password123'
        self.form_input['password_confirmation'] = 'password123'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the form not accepting a password field with no lowercase characters in it
    def test_password_must_contain_lowercase_character(self):
        self.form_input['new_password'] = 'PASSWORD123'
        self.form_input['password_confirmation'] = 'PASSWORD123'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the form not accepting a password field with no numbers in it
    def test_password_must_contain_number(self):
        self.form_input['new_password'] = 'PasswordABC'
        self.form_input['password_confirmation'] = 'PasswordABC'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the new_password and password_confirmation fields should be equal for a valid form
    def test_new_password_and_password_confirmation_are_identical(self):
        self.form_input['password_confirmation'] = 'WrongPassword123'
        form = StudentSignUpForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    

    # Test if the form saves correctly
    def test_form_must_save_correctly(self):
        form = StudentSignUpForm(data=self.form_input)
        before_count = User.objects.count()
        form.save()
        after_count = User.objects.count()
        self.assertEqual(after_count, before_count+1)
        user = User.objects.get(username='janedoe')
        self.assertEqual(user.first_name, 'Jane')
        self.assertEqual(user.last_name, 'Doe')
        self.assertEqual(user.email, 'janedoe@example.org')
        is_password_correct = check_password('Password123', user.password)
        self.assertTrue(is_password_correct)
