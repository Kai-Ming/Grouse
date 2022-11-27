from django.test import TestCase
from django.core.exceptions import ValidationError
from lessons.models import Student


class StudentModelTestCase(TestCase):
    """Unit tests for the Student model."""

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

    def test_valid_user(self):
        self._assert_user_is_valid()

    # Student no
    def test_student_no_must_be_unique(self):
        second_user = self._create_second_user()
        self.user.student_no = second_user.student_no
        self._assert_user_is_invalid()

    def test_student_no_must_be_a_positive_integer(self):
        self.user.student_no = -1
        self._assert_user_is_invalid()

    # add test cases as the Student model is extended

    # Helper functions
    def _assert_user_is_valid(self):
        try:
            self.user.full_clean()
        except ValidationError:
            self.fail('Test user is not valid.')

    def _assert_user_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.user.full_clean()

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
