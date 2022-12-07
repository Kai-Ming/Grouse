"""Unit tests for the lesson request form"""
from django.test import TestCase
from lessons.models import User, Lesson
from lessons.forms import LessonRequestForm

class LessonRequestFormTestCase(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

    def setUp(self):
        self.user = User.objects.get(username='johndoe')

    def test_valid_number_of_lessons(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid())

    def test_invalid_number_of_lessons(self):
        input = {'number_of_lessons': 10, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertFalse(form.is_valid())

    def test_valid_lesson_duration(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid()) 

    def test_invalid_lesson_duration(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 31, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertFalse(form.is_valid())

    def test_teacher_can_be_empty(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': ''}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid()) 
