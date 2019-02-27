from raven.contrib.flask import Client

from sensys.contrib import SenSysClient


class FlaskSenSysClient(SenSysClient, Client):
    pass
