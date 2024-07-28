from django.db.models import F
from django.utils import timezone

from mailings.models import Mailing, MailingAttempt


def sending_script():
    now = timezone.now()
    Mailing.objects.filter(started_at__lte=now, completed_at__gt=now).update(status='SENDING')
    Mailing.objects.filter(completed_at__lte=now).update(status='COMPLETED')

    query_set_sent_earlier = Mailing.objects.filter(status='SENDING').filter(
        last_attempt_at__lt=now - F('sending_interval'))
    query_set_new = Mailing.objects.filter(status='SENDING').filter(
       last_attempt_at__isnull=True).prefetch_related('message', 'clients')

    attempts = []

    for mailing in query_set_sent_earlier:
        mailing_attempts = mailing.try_n_attempts(now)
        attempts.extend(mailing_attempts)

    for mailing in query_set_new:
        mailing_attempts = mailing.try_n_attempts(now)
        attempts.extend(mailing_attempts)

    MailingAttempt.objects.bulk_create(attempts)

    query_set_new.update(last_attempt_at=now)
    query_set_sent_earlier.update(last_attempt_at=now)

