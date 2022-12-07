from django.urls import reverse
from lessons.models import Lesson

def reverse_with_next(url_name, next_url):
    url = reverse(url_name)
    url += f"?next={next_url}"
    return url

def create_lesson_request(student, from_count, to_count):
    """Create a lesson request for testing purposes."""
    for count in range(from_count, to_count):
        teacher = f'Teacher{count}'
        lesson = Lesson(student=student, number_of_lessons=1, lesson_duration=30, teacher=teacher)
        lesson.save()

class LogInTester:
    def _is_logged_in(self):
        return '_auth_user_id' in self.client.session.keys()
