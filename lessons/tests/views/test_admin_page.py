"""Tests of the admin page view."""
from django.test import TestCase
from django.urls import reverse
from lessons.forms import LessonRequestForm
from lessons.models import User
from lessons.tests.helpers import reverse_with_next, create_lesson_request


class UserPageViewTestCase(TestCase):
    """Tests of the admin view."""

    fixtures = [
        'lessons/tests/fixtures/default_admin.json',
        'lessons/tests/fixtures/default_superadmin.json',
    ]


    # Creates admin and superadmin instances to be used for tests and saves the url of the admin_page
    def setUp(self):
        self.admin = User.objects.get(username='jackdoe')
        self.superadmin = User.objects.get(username='janedoe')
        self.url = reverse('admin_page')


    # Tests if the admin_page name has the correct url associated with it
    def test_user_page_url(self):
        self.assertEqual(self.url,'/admin_page/')


    # Tests if an admin can log into the admin page
    def test_get_admin_page_with_admin(self):
        self.client.login(username=self.admin.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    
    # Tests if a superadmin can log into the admin page
    def test_get_admin_page_with_superadmin(self):
        self.client.login(username=self.superadmin.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
    

    # Tests if the admin page redirects when a not logged in user tries to enter
    def test_get_page_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)

    