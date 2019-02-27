import datetime
import json
from logging import makeLogRecord
from logging.handlers import SysLogHandler


class SenSysClient:

    FAKE_DSN = '//key@domain/project'

    def __init__(self, *args, **kwargs):
        self.handler = SysLogHandler(address='/dev/log')
        # it is important to separate `ident` with whitespace for syslog protocol
        self.handler.ident = self.get_tag() + ' '
        super().__init__(*args, **kwargs)

    def get_tag(self):
        raise NotImplementedError

    def set_dsn(self, dsn=None, transport=None):
        # it is important to pass `dsn` into `DjangoClient`,
        # otherwise we could not retrieve message in `self.send()`
        dsn = 'http:{}'.format(self.FAKE_DSN) if dsn is None else dsn
        super().set_dsn(dsn, transport)

    def send(self, auth_header=None, **data):
        # support for standard Sentry Clients through `sensys` client
        if self.get_public_dsn() != self.FAKE_DSN:
            return super().send(auth_header, **data)

        message = json.dumps(data, default=self.datetime_decode)
        self.handler.emit(makeLogRecord({'msg': message}))

    @staticmethod
    def datetime_decode(obj):
        if isinstance(obj, (datetime.datetime, datetime.date, datetime.time)):
            return obj.isoformat()
