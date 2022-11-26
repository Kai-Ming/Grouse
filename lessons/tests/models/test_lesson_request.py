from django.core.exceptions import ValidationError
from django.test import TestCase
from lessons.models import LessonRequest, User

class LessonRequestTest(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

    def setUp(self):
        super(TestCase, self).setUp()
        self.user = User.objects.get(username='johndoe')
        self.lesson_request = LessonRequest(
            student=self.user,
            number_of_lessons=1,
            lesson_duration=45,
            teacher='Jeoren Keppens'
        )

    def test_student_must_not_be_blank(self):
        self.lesson_request.student = None
        self._assert_lesson_request_is_invalid()

    def test_teacher_can_be_blank(self):
        self.lesson_request.teacher = ''
        self._assert_lesson_request_is_valid()

    def test_number_of_lessons_cannot_be_negative(self):
        self.lesson_request.number_of_lessons = -1
        self._assert_lesson_request_is_invalid()

    def test_lesson_duration_cannot_be_negative(self):
        self.lesson_request.lesson_duration = -1
        self._assert_lesson_request_is_invalid()

    def _assert_lesson_request_is_valid(self):
        try:
            self.lesson_request.full_clean()
        except (ValidationError):
            self.fail('Test lesson request should be valid')

    def _assert_lesson_request_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.lesson_request.full_clean()