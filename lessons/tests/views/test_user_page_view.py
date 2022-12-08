"""Tests of the user page view."""
from django.test import TestCase
from django.urls import reverse
from lessons.forms import LessonRequestForm
from lessons.models import User
from lessons.tests.helpers import reverse_with_next, create_lesson_request


class UserPageViewTestCase(TestCase):
    """Tests of the feed view."""

    fixtures = [
        'lessons/tests/fixtures/default_student.json',
    ]

    # Sets up an user to be used for the tests and stores the url of the user_page page
    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.url = reverse('user_page')


    # Tests if the user_page name points towards the correct URL
    def test_user_page_url(self):
        self.assertEqual(self.url,'/user_page/')


    # Tests if the user page renders correctly
    def test_get_user_page(self):
        self.client.login(username=self.user.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


    # Tests if the user page correctly redirects if a user is not logged in
    def test_get_page_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)


    # Tests if the lesson request list renders correctly
    def test_lesson_request_shows_correct_list(self):
        self.client.login(username=self.user.username, password='Password123')
        create_lesson_request(self.user, 100, 103)
        response = self.client.get(self.url)
        for count in range(100, 103):
            self.assertContains(response, f'Teacher{count}')