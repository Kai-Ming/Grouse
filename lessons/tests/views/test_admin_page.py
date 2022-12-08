"""Tests of the user page view."""
from django.test import TestCase
from django.urls import reverse
from lessons.forms import LessonRequestForm
from lessons.models import User
from lessons.tests.helpers import reverse_with_next, create_lesson_request


class UserPageViewTestCase(TestCase):
    """Tests of the feed view."""

    fixtures = [
        'lessons/tests/fixtures/default_admin.json',
        'lessons/tests/fixtures/default_superadmin.json',
    ]

    def setUp(self):
        self.user = User.objects.get(username='johndoe')
        self.admin = User.objects.get(username='jackdoe')
        self.superadmin = User.objects.get(username='janedoe')
        self.url = reverse('admin_page')

    def test_user_page_url(self):
        self.assertEqual(self.url,'/admin_page/')

    def test_get_admin_page_with_admin(self):
        self.client.login(username=self.admin.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_get_admin_page_with_superadmin(self):
        self.client.login(username=self.superadmin.username, password='Password123')
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
 
    def test_get_page_redirects_when_not_logged_in(self):
        redirect_url = reverse_with_next('log_in', self.url)
        response = self.client.get(self.url)
        self.assertRedirects(response, redirect_url, status_code=302, target_status_code=200)

    