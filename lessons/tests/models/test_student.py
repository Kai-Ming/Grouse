from django.test import TestCase
from django.core.exceptions import ValidationError
from lessons.models import Student


class StudentModelTestCase(TestCase):
    """Unit tests for the Student model."""


    # Sets up example student to be used for tests
    def setUp(self):
        self.user = Student.objects.create_user(
            user_type=1,
            username='johndoe',
            first_name='John',
            last_name='Doe',
            email='johndoe@example.org',
            password='Password123',
            student_no=1234
        )


    # Tests if a student is valid
    def test_valid_user(self):
        self._assert_user_is_valid()


    # Tests the fact that the student_no field of a student should be unique
    def test_student_no_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.student_no = second_user.student_no
        self._assert_user_is_invalid()
    

    # Tests the fact that the student_no field of a student should be a positive integer
    def test_student_no_must_be_a_positive_integer(self):
        self.user.student_no = -1
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
        user = Student.objects.create_user(
            user_type=1,
            username='janedoe',
            first_name='Jane',
            last_name='Doe',
            email='janedoe@example.org',
            password='Password123',
            student_no=4321
        )
        return user
