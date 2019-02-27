from django.conf import settings
from raven.contrib.django.client import DjangoClient

from sensys.contrib import SenSysClient


class DjangoSenSysClient(SenSysClient, DjangoClient):
    def get_tag(self):
        return settings.SENSYS_TAG
