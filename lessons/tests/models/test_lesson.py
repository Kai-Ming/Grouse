from django.core.exceptions import ValidationError
from django.test import TestCase
from lessons.models import Lesson, User
import datetime


class LessonTest(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

    def setUp(self):
        super(TestCase, self).setUp()
        self.user = User.objects.get(username='johndoe')
        self.lesson = Lesson(
            student=self.user,
            start_date = datetime.datetime(2023, 5, 17),
            number_of_lessons=1,
            lesson_duration=45,
            teacher='Jeoren Keppens',
            price=200.50,
            fulfilled=True
        )

    def test_student_must_not_be_blank(self):
        self.lesson.student = None
        self._assert_lesson_is_invalid()

    def test_teacher_cannot_be_blank(self):
        self.lesson.teacher = ''
        self._assert_lesson_is_valid()

    def test_number_of_lessons_cannot_be_negative(self):
        self.lesson.number_of_lessons = -1
        self._assert_lesson_is_invalid()

    def test_lesson_duration_cannot_be_negative(self):
        self.lesson.lesson_duration = -1
        self._assert_lesson_is_invalid()

    def test_price_must_be_positive(self):
        self.lesson.price = -1
        self._assert_lesson_is_invalid()

    def _assert_lesson_is_valid(self):
        try:
            self.lesson.full_clean()
        except ValidationError:
            self.fail('Test lesson booking should be valid')

    def _assert_lesson_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.lesson.full_clean()
