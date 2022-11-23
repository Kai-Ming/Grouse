from django.core.management.base import BaseCommand, CommandError
from faker import Faker
from lessons.models import User
from django.db.utils import IntegrityError

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
                self._create_user(1)
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

        User.objects.create_user(
            username,
            user_type = type,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=Command.PASSWORD,
        )

    def _email(self, first_name, last_name):
        email = f'{first_name}.{last_name}@example.org'
        return email

    def _username(self, first_name, last_name):
        username = f'{first_name}{last_name}'
        return username
