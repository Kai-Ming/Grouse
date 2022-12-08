"""Tests of the lesson request view."""
from django.test import TestCase
from django.urls import reverse
from lessons.forms import LessonRequestForm
from lessons.models import User, Lesson
from lessons.tests.helpers import reverse_with_next, create_lesson_request

class LessonRequestViewTestCase(TestCase):
    """Tests of the lesson request view."""

    fixtures = ['lessons/tests/fixtures/default_student.json']


    # Creates a user instance and example form imput to be used for tests and saves the url of the lesson_request page
    def setUp(self):
        self.url = reverse('lesson_request')
        self.form_input = {'number_of_lessons': 1, 'lesson_duration': 30, 'teacher': 'Jane Doe'}
        self.user = User.objects.get(username='johndoe')


    # Tests if the lesson_request name has the correct url associated with it
    def test_lesson_request_url(self):
        self.assertEqual(self.url,'/lesson_request/')


    # Tests if the correct page is rendered for lesson request
    def test_get_lesson_request(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(isinstance(form, LessonRequestForm))
        self.assertFalse(form.is_bound)


    # Tests if the an invalid lesson request produces the desired results
    def test_unsuccessful_lesson_request(self):
        self.form_input['number_of_lessons'] = -1
        self.client.login(username=self.user.username, password='Password123')
        before_count = Lesson.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = Lesson.objects.count()
        self.assertEqual(after_count, before_count)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lesson_request.html')
        form = response.context['form']
        self.assertTrue(isinstance(form, LessonRequestForm))
        self.assertTrue(form.is_bound)


    # Tests if the a valid lesson request produces the desired results
    def test_successful_lesson_request(self):
        self.client.login(username=self.user.username, password='Password123')
        before_count = Lesson.objects.count()
        response = self.client.post(self.url, self.form_input)
        after_count = Lesson.objects.count()
        self.assertEqual(after_count, before_count+1)
