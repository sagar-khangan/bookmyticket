import logging
import sys


def get_logger(app_name):
    root = logging.getLogger(__name__)
    root.setLevel(logging.DEBUG)

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    FORMAT = "[%(levelname)s] %(asctime)s [%(filename)s:%(lineno)s] %(message)s"
    formatter = logging.Formatter(FORMAT)
    ch.setFormatter(formatter)
    root.addHandler(ch)
    return root
