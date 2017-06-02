from django.contrib.auth.models import User
from django.core.management import BaseCommand
from weshop.config import config


class Command(BaseCommand):
    help = "Create super user for Django admin."

    def handle(self, *args, **options):
        User.objects.create_superuser(username=config.SUPERUSER_USERNAME, password=config.SUPERUSER_PASSWORD, email=config.SUPERUSER_EMAIL)
        self.stdout.write("Super User created successfully!")