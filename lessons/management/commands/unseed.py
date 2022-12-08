from django.core.management.base import BaseCommand, CommandError
from lessons.models import User, Lesson, Invoice, Transfer

class Command(BaseCommand):
    def handle(self, *args, **options):
        User.objects.filter(is_staff=False, is_superuser=False).delete()
        Lesson.objects.all().delete()
        Invoice.objects.all().delete()
        Transfer.objects.all().delete()
