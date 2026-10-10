from datetime import datetime
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from threading import Event
from threading import Thread
from time import sleep

from analysis import Analysis
from logs import Logs
from trading import Trading
from twitter import Twitter

# Whether to send all logs to the cloud instead of a local file.
LOGS_TO_CLOUD = True

# The duration of the smallest backoff step in seconds.
BACKOFF_STEP_S = 0.1

# The maximum number of retry steps, equivalent to 0.1 * (2^12 - 1) = 409.5
# seconds of total delay. This is the largest interval that one backoff
# sequence may take.
MAX_TRIES = 12

# The time in seconds after which to reset a backoff sequence. This is the
# smallest interval at which backoff sequences may repeat normally.
BACKOFF_RESET_S = 30 * 60

# The host for the monitor Web server.
MONITOR_HOST = '0.0.0.0'

# The port for the monitor Web server.
MONITOR_PORT = 80

# The message returned by the monitor Web server.
MONITOR_MESSAGE = 'OK'


class Monitor:
    pass  # TODO: implement

    def __init__(self):
        pass  # TODO: implement


    def start(self):
        pass  # TODO: implement


    def stop(self):
        pass  # TODO: implement


    class MonitorHandler(BaseHTTPRequestHandler):
        pass  # TODO: implement

        def _set_headers(self):
            pass  # TODO: implement

        def do_GET(self):
            pass  # TODO: implement

        def do_HEAD(self):
            pass  # TODO: implement


class Main:
    pass  # TODO: implement

    def __init__(self):
        pass  # TODO: implement

    def twitter_callback(self, tweet):
        pass  # TODO: implement





    def run_session(self):
        pass  # TODO: implement


    def backoff(self, tries):
        pass  # TODO: implement


    def run(self):
        pass  # TODO: implement









if __name__ == '__main__':
