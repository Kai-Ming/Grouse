"""Unit tests for the lesson request form"""
from django.test import TestCase
from lessons.models import User, Lesson
from lessons.forms import LessonRequestForm

class LessonRequestFormTestCase(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

    # Sets up example user to be used for tests
    def setUp(self):
        self.user = User.objects.get(username='johndoe')
    

    # Test the form is valid with the valid input for number_of_lessons field
    def test_valid_number_of_lessons(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid())


    # Test the form is invalid with the invalid input for number_of_lessons field
    def test_invalid_number_of_lessons(self):
        input = {'number_of_lessons': 10, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertFalse(form.is_valid())


    # Test the form is valid with the valid input for lesson_duration field
    def test_valid_lesson_duration(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid()) 


    # Test the form is valid with the invalid input for lesson_duration field
    def test_invalid_lesson_duration(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 31, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertFalse(form.is_valid())


    # Test the form is valid with the teacher field empty
    def test_teacher_can_be_empty(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': ''}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid()) 
