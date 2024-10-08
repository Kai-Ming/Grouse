from django.test import TestCase
from django.core.exceptions import ValidationError
from lessons.models import User


class UserModelTestCase(TestCase):
    """Unit tests for the User model."""


    # Sets up example user to be used for tests
    def setUp(self):
        self.user = User.objects.create_user(
            user_type=1,
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123'
        )


    # Tests if a user is valid
    def test_valid_user(self):
        self._assert_user_is_valid()


    # Tests the fact that the user_type field of a user should be valid (between 1 and 5 inclusive)
    def test_user_must_have_a_valid_type(self):
        self.user.user_type = -1
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user should be not blank
    def test_username_cannot_be_blank(self):
        self.user.username = ''
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user can be 16 characters long
    def test_username_can_be_16_characters_long(self):
        self.user.username = 'x' * 16
        self._assert_user_is_valid()


    # Tests the fact that the username field of a user shouldn't be over 16 characters
    def test_username_cannot_be_over_16_characters_long(self):
        self.user.username = 'x' * 17
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user should be unique
    def test_username_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.username = second_user.username
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user should only have alphanumericals
    def test_username_must_contain_only_alphanumericals(self):
        self.user.username = 'john!doe'
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user should at least have 3 alphanumericals
    def test_username_must_contain_at_least_3_alphanumericals(self):
        self.user.username = 'jo'
        self._assert_user_is_invalid()


    # Tests the fact that the username field of a user can have numbers
    def test_username_may_contain_numbers(self):
        self.user.username = 'j0hndoe2'
        self._assert_user_is_valid()


   # Tests the fact that the first_name field of a user shouldn't be blank
    def test_first_name_must_not_be_blank(self):
        self.user.first_name = ''
        self._assert_user_is_invalid()


    # Tests the fact that the first_name field of a user shouldn't be over 50 characters long
    def test_first_name_cannot_be_over_50_characters_long(self):
        self.user.first_name = 'x' * 51
        self._assert_user_is_invalid()

    
    # Tests the fact that the last_name field of a user shouldn't be blank
    def test_last_name_must_not_be_blank(self):
        self.user.last_name = ''
        self._assert_user_is_invalid()


    # Tests the fact that the last_name field of a user shouldn't be over 50 characters long
    def test_last_name_cannot_be_over_50_characters_long(self):
        self.user.last_name = 'x' * 51
        self._assert_user_is_invalid()


    # Tests the fact that the email field of a user shouldn't be blank
    def test_email_must_not_be_blank(self):
        self.user.email = ''
        self._assert_user_is_invalid()


    # Tests the fact that the email field of a user should be unique
    def test_email_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.email = second_user.email
        self._assert_user_is_invalid()


    """Helper functions"""

    # Assert a user is valid
    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except ValidationError:
            self.fail('Test user is not valid.')


    # Assert a user is invalid
    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()


    # Create a second user
    def _create_second_user(self):
        user = User.objects.create_user(
            user_type=1,
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123'
        )
        return user
