from django.conf import settings
from django.core.cache import cache
from django.db.models import F
from django.utils import timezone

from blog.models import Post
from mailings.models import Mailing, MailingAttempt


def sending_script():
    """
    Main sending script
    """
    now = timezone.now()
    not_banned_mailings = Mailing.objects.exclude(is_banned=True)
    active_mailings = not_banned_mailings.filter(status='SENDING').filter(started_at__lte=now, completed_at__gt=now)

    query_set_sent_earlier = active_mailings.filter(last_attempt_at__lt=now - F('sending_interval'))
    query_set_new = active_mailings.filter(last_attempt_at__isnull=True).prefetch_related('message', 'clients')

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


def get_posts_from_cache():
    """
    Get posts from cache, if cache is empty, get posts from DB
    """
    if settings.CACHE_ENABLED:
        key = 'posts_list'
        posts = cache.get(key)

        if posts is None:
            posts = Post.objects.order_by("?")[:3]
            cache.set(key, posts)
        return posts

    return Post.objects.order_by("?")[:3]
