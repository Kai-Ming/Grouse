"""Tests of the log out view."""
from django.test import TestCase
from django.urls import reverse
from lessons.models import User
from lessons.tests.helpers import LogInTester

class LogOutViewTestCase(TestCase, LogInTester):
    """Tests of the log out view."""

    fixtures = ['lessons/tests/fixtures/default_student.json']


    # Sets up an example User object to be used for tests and store the log_out url
    def setUp(self):
        self.url = reverse('log_out')
        self.user = User.objects.get(username='johndoe')


    # Tests if the log_out name points towards the correct URL
    def test_log_out_url(self):
        self.assertEqual(self.url,'/log_out/')


    # Tests if the log_in page renders correctly 
    def test_get_log_out(self):
        self.client.login(username='johndoe', password='Password123')
        self.assertTrue(self._is_logged_in())
        response = self.client.get(self.url, follow=True)
        response_url = reverse('log_in')
        self.assertRedirects(response, response_url, status_code=302, target_status_code=200)
        self.assertTemplateUsed(response, 'log_in.html')
        self.assertFalse(self._is_logged_in())

