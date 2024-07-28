from celery import shared_task

from services.utils import sending_script


@shared_task
def send_mails():
    """
    Celery task for sending mails.
    """
    sending_script()
