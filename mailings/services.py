from django.db.models import F
from django.utils import timezone

from mailings.models import Mailing, MailingAttempt


def sending_script():
    now = timezone.now()
    Mailing.objects.filter(started_at__le=now, completed_at__gt=now).update(status='SENDING')
    Mailing.objects.filter(completed_at__le=now).update(status='COMPLETED')

    query_set = Mailing.objects.filter(status='SENDING').filter(
        last_attempt_at__lt=now - F('sending_interval')).prefetch_related('message', 'clients')
    attempts = []

    for mailing in query_set:
        mailing_attempts = mailing.try_n_attempts(now)
        attempts.append(mailing_attempts)

    MailingAttempt.objects.bulk_create(attempts)
    query_set.update(last_attempt_at=now)
