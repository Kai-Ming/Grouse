"""Unit tests of the log in form."""
from django import forms
from django.test import TestCase
from lessons.forms import LogInForm
from lessons.models import User

class LogInFormTestCase(TestCase):
    """Unit tests of the log in form."""

    fixtures = ['lessons/tests/fixtures/default_student.json']

    #Set up an examplery input to use for the tests
    def setUp(self):
        self.form_input = {'username': 'janedoe', 'password': 'Password123'}


    # Test the form having the required fields inside it
    def test_form_contains_required_fields(self):
        form = LogInForm()
        self.assertIn('username', form.fields)
        self.assertIn('password', form.fields)
        password_field = form.fields['password']
        self.assertTrue(isinstance(password_field.widget,forms.PasswordInput))


    # Test if the form accepts valid input
    def test_form_accepts_valid_input(self):
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Test if the form rejects a blank username field
    def test_form_rejects_blank_username(self):
        self.form_input['username'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())
    

    # Test if the form rejects a blank password field
    def test_form_rejects_blank_password(self):
        self.form_input['password'] = ''
        form = LogInForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test if the form accepts an incorrect username field
    def test_form_accepts_incorrect_username(self):
        self.form_input['username'] = 'ja'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Test if the form accepts an incorrect password field
    def test_form_accepts_incorrect_password(self):
        self.form_input['password'] = 'pwd'
        form = LogInForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Test if the form can authenticate a valid user
    def test_can_authenticate_valid_user(self):
        fixture = User.objects.get(username='johndoe')
        form_input = {'username': 'johndoe', 'password': 'Password123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, fixture)


    # Test if the form refuses to authenticate an invalid user
    def test_invalid_credentials_do_not_authenticate(self):
        form_input = {'username': 'johndoe', 'password': 'WrongPassword123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)


    # Test if the form refuses to authenticate an user with a blank password field
    def test_blank_password_does_not_authenticate(self):
        form_input = {'username': 'johndoe', 'password': ''}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)


    # Test if the form refuses to authenticate an user with a blank username field
    def test_blank_username_does_not_authenticate(self):
        form_input = {'username': '', 'password': 'Password123'}
        form = LogInForm(data=form_input)
        user = form.get_user()
        self.assertEqual(user, None)

