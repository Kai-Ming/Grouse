"""Unit tests for the lesson request form"""
from django.test import TestCase
from lessons.models import User, Lesson
from lessons.forms import LessonRequestForm

class LessonRequestFormTestCase(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

    
    # Sets up example user to be used for tests
    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.form_input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'Jane Doe'}

        
    # Test the form is valid with the valid input for number_of_lessons field
    def test_valid_number_of_lessons(self):
        form = LessonRequestForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Test the form is invalid with the invalid input for number_of_lessons field
    def test_invalid_number_of_lessons(self):
        self.form_input['number_of_lessons'] = -1
        form = LessonRequestForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the form is valid with the valid input for lesson_duration field
    def test_valid_lesson_duration(self):
        input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'A'}
        form = LessonRequestForm(data=input)
        self.assertTrue(form.is_valid()) 


    # Test the form is valid with the invalid input for lesson_duration field
    def test_invalid_lesson_duration(self):
        self.form_input['lesson_duration'] = -1
        form = LessonRequestForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Test the form is valid with the teacher field empty
    def test_teacher_can_be_empty(self):
        self.form_input['teacher'] = ''
        form = LessonRequestForm(data=self.form_input)
        self.assertTrue(form.is_valid())
