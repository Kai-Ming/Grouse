"""Unit tests for the lesson edit form"""
from django.test import TestCase
from lessons.models import User, Lesson
from lessons.forms import LessonEditForm
import datetime

class LessonEditFormTestCase(TestCase):

    fixtures = ['lessons/tests/fixtures/default_student.json']

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
    
    def test_form_has_necessary_fields(self):
        form = LessonEditForm()
        self.assertIn('start_date', form.fields)
        self.assertIn('number_of_lessons', form.fields)
        self.assertIn('lesson_duration', form.fields)
        self.assertIn('teacher', form.fields)
        self.assertIn('price', form.fields)
        self.assertIn('fulfilled', form.fields)

    def test_valid_form(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_price_cant_be_negative(self):
        self.form_input['price'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_valid_number_of_lessons(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())

    def test_invalid_number_of_lessons(self):
        self.form_input['number_of_lessons'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())

    def test_valid_lesson_duration(self):
        form = LessonEditForm(data=self.form_input)
        self.assertTrue(form.is_valid())
    
    def test_invalid_lesson_duration(self):
        self.form_input['lesson_duration'] = -1
        form = LessonEditForm(data=self.form_input)
        self.assertFalse(form.is_valid())