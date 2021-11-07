import os
import time
from logging import INFO, WARNING, FileHandler, StreamHandler, basicConfig, getLogger

from safety.tools import *
from telethon import __version__

from ..version import __version__ as __pySNEHABHI__
from ..version import snehabhi_version

if os.path.exists("ultroid.log"):
    os.remove("ultroid.log")

LOGS = getLogger("pyUltLogs")
TeleLogger = getLogger("Telethon")
TeleLogger.setLevel(WARNING)

basicConfig(
    format="%(asctime)s || %(name)s [%(levelname)s] : %(message)s",
    level=INFO,
    datefmt="%m/%d/%Y, %H:%M:%S",
    handlers=[FileHandler("ultroid.log"), StreamHandler()],
)

LOGS.info(
    """
                -----------------------------------
                        Starting Deployment
                -----------------------------------
"""
)


LOGS.info(f"py-Snehabhi Version - {__pySNEHABHI__}")
LOGS.info(f"Telethon Version - {__version__}")
LOGS.info(f"Snehabhi Version - {snehabhi_version}")
