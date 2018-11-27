import sys
import json
import argparse

from string import whitespace

from .errors import error, plugin_error

try:
    # noinspection PyUnresolvedReferences
    from raven.base import Client
    # noinspection PyUnresolvedReferences
    from raven.exceptions import InvalidDsn
except ImportError as exc:
    error()


# global definitions
separator, clients = None, {}


def init():
    """
        Initialize plugin to start receiving messages from rsyslog.
    """

    global separator, clients

    # step 1: collect passed arguments
    parser = argparse.ArgumentParser(description='Sen(try)Sys(log) plugin.')
    parser.add_argument(
        '-s', '--separator', type=str, metavar='SEP',
        help='syslog sends raw string and this argument specify how separate `syslogtag` from `msg` body'
    )
    parser.add_argument(
        '-m', '--mapping', type=str, metavar='PATH',
        help='absolute path to SenSys `json` mapping: "syslogtag": "dsn"'
    )
    args = parser.parse_args()

    # step 2: check passed argument values
    if args.separator is None:
        raise argparse.ArgumentError(args.separator, '-s | --separator is not specified')
    if args.mapping is None:
        raise argparse.ArgumentError(args.mapping, '-c | --mapping is not specified')

    with open(args.mapping) as f:
        mapping = json.load(f)

    # step 3: initialize global definitions
    clients = {tag: Client(dsn) for tag, dsn in mapping.items()}
    separator = args.separator


def process():
    """
        Process handlers for all received messages from rsyslog.
    """

    for line in sys.stdin:
        line = line.strip(whitespace)

        # if line was whitespace only, like `\n\t` etc.
        if not line:
            continue

        tag, msg = map(lambda x: x.strip(whitespace), line.split(separator))
        client = clients.get(tag)
        if client is not None:
            client.send(auth_header=None, **json.loads(msg))

    # if no `sys.stdin` present
    else:
        sys.exit(0)


@plugin_error
def main():
    init()
    process()


if __name__ == '__main__':
    main()
