from django.utils import timezone

from mailings.models import Mailing

from celery import shared_task

@shared_task
def send_mails():
    now = timezone.now()
    Mailing.objects.filter()