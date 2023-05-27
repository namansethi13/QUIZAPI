
import datetime
from .models import Quiz
import logging
from django_crontab import periodic_task, crontab

logger = logging.getLogger(__name__)

def change_status():
    logger.info("done")
    now = datetime.datetime.now()
    Quiz.objects.filter(startDate__gt=now, status='active').update(status='inactive')
    Quiz.objects.filter(startDate__lte=now, endDate__gte=now, status='inactive').update(status='active')
    Quiz.objects.filter(endDate__lt=now, status='active').update(status='finished')

