from django.apps import AppConfig
from django.conf import settings
from django.core import exceptions

from raven.contrib.django.models import initialize


class SenSysConfig(AppConfig):

    name = 'sensys.contrib.django'
    label = 'sensys_contrib_django'
    verbose_name = 'SenSys'

    def ready(self):
        # step 1: check custom sensys settings
        if not getattr(settings, 'SENTRY_CLIENT', False):
            setattr(settings, 'SENTRY_CLIENT', 'sensys.contrib.django.DjangoSenSysClient')
        if not getattr(settings, 'SENSYS_TAG', False):
            raise exceptions.ImproperlyConfigured('SENSYS_TAG setting is not define.')
        # step 2: initialize raven client
        initialize()
