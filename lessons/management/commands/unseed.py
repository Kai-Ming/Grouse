from django.core.management.base import BaseCommand, CommandError
from lessons.models import User

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.all().delete()
