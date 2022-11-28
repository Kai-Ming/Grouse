from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from lessons.models import User, Lesson
from django.db.utils import IntegrityError
import datetime
import random

class Command(BaseCommand):
    PASSWORD = "Password123"
    USER_COUNT = 100

    def __init__(self):
        super().__init__()
        self.faker = Faker('en_GB')

    def handle(self, *args, **options):
        user_count = 0
        # Seeds students
        while user_count < Command.USER_COUNT:
            print(f'Seeding user {user_count}',  end='\r')
            try:
                student = self._create_user(1)
                try:
                    self._create_lesson(student)
                except (IntegrityError):
                    continue
            except (IntegrityError):
                continue
            user_count += 1

        # Seeds admins and superadmins
        try:
            self._create_user(4)
            self._create_user(4)
            self._create_user(5)
            user_count += 3
        except (IntegrityError):
            print('Failed admin seeding')

        print('User seeding complete')

    # Creates a random user
    def _create_user(self, type):
        first_name = self.faker.first_name()
        last_name = self.faker.last_name()
        email = self._email(first_name, last_name)
        username = self._username(first_name, last_name)
        is_superuser = False
        is_staff = False
        if (type == 5):
            is_superuser = True
            is_staff = True
            print(username + " ")

        student = User.objects.create_user(
            username,
            user_type = type,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=Command.PASSWORD,
            is_superuser = is_superuser,
            is_staff = is_staff,
        )
        return student

    def _email(self, first_name, last_name):
        email = f'{first_name}.{last_name}@example.org'
        return email

    def _username(self, first_name, last_name):
        username = f'{first_name}{last_name}'
        return username

    # Creates a lesson request for the student
    def _create_lesson(self, student):
        number_of_lessons = random.randint(1,2)
        lesson_duration = random.choice([30,45,60])
        fulfilled = bool(random.getrandbits(1))
        paid_type = random.randint(1,4)
        price = random.randint(100, 400)
        teacher = self.faker.first_name() + " " + self.faker.last_name()
        start_date = datetime.date.today()
        
        lesson = Lesson(
            student = student,
            start_date = start_date,
            number_of_lessons = number_of_lessons,
            lesson_duration = lesson_duration,
            teacher = teacher,
            price = price,
            fulfilled = fulfilled, 
            paid_type = paid_type
        )    
        lesson.save()    
