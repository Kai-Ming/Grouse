"""Unit tests for the lesson edit form"""
from django.test import TestCase
from lessons.models import User, Lesson
from lessons.forms import LessonEditForm
import datetime

class LessonEditFormTestCase(TestCase):
    """Tester Class for Lesson Edit Form"""


    fixtures = ['lessons/tests/fixtures/default_student.json']

    # Set up an example user and example form input for the tests
    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.form_input = {
            'start_date': datetime.date.today(), 
            'number_of_lessons': 1, 
            'lesson_duration': 30, 
            'teacher': 'Jane Doe', 
            'price': 10.00, 
            'fulfilled': True
        }
    

    # Check that the form has the necessary fields
    def test_form_has_necessary_fields(self):
        form = LessonEditForm()
        self.assertIn('start_date', form.fields)
        self.assertIn('number_of_lessons', form.fields)
        self.assertIn('lesson_duration', form.fields)
        self.assertIn('teacher', form.fields)
        self.assertIn('price', form.fields)
        self.assertIn('fulfilled', form.fields)


    # Check that the form is valid given valid input
    def test_valid_form(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    

    # Check that the price field cannot be negative
    def test_price_cant_be_negative(self):
        self.form_input['price'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Check that when number_of_lessons field is valid, the form is valid
    def test_valid_number_of_lessons(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())


    # Check that when number_of_lessons field is invalid, the form is invalid
    def test_invalid_number_of_lessons(self):
        self.form_input['number_of_lessons'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())


    # Check that when valid_lesson field is valid, the form is valid
    def test_valid_lesson_duration(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    

    # Check that when valid_lesson field is invalid, the form is invalid
    def test_invalid_lesson_duration(self):
        self.form_input['lesson_duration'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())