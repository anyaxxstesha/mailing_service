from django.core.management import BaseCommand

from mailings.services import sending_script


class Command(BaseCommand):
    def handle(self, *args, **options):
        sending_script()
