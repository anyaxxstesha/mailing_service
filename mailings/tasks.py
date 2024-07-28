from django.db.models import F
from django.utils import timezone

from mailings.models import Mailing, MailingAttempt

from celery import shared_task
from mailings.services import sending_script


@shared_task
def send_mails():
    sending_script()
