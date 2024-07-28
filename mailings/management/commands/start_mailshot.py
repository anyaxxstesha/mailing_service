from django.core.management import BaseCommand

from services.utils import sending_script


class Command(BaseCommand):
    def handle(self, *args, **options):
        sending_script()
