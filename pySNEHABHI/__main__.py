import os
import sys
import time

from . import *
from .functions.helper import time_formatter, updater
from .startup.funcs import autopilot, customize, plug, ready, startup_stuff
from .startup.loader import load_other_plugins

# Option to Auto Update On Restarts..
if udB.get("UPDATE_ON_RESTART") and os.path.exists(".git") and updater():
    os.system("git pull -f -q && pip3 install --no-cache-dir -U -q -r requirements.txt")
    os.execl(sys.executable, "python3", "-m", "pyUltroid")

startup_stuff()


snehabhi_bot.me.phone = None
snehabhi_bot.first_name = ultroid_bot.me.first_name

if not snehabhi_bot.me.bot:
    udB.set("OWNER_ID", ultroid_bot.uid)


LOGS.info("Initialising...")


snehabhi_bot.run_in_loop(autopilot())

pmbot = udB.get("PMBOT")
manager = udB.get("MANAGER")
addons = udB.get("ADDONS") or Var.ADDONS
vcbot = udB.get("VCBOT") or Var.VCBOT

# Railway dont allow Music Bots
if HOSTED_ON == "railway" and not vcbot:
    vcbot = "False"

load_other_plugins(addons=addons, pmbot=pmbot, manager=manager, vcbot=vcbot)

suc_msg = """
            ----------------------------------------------------------------------
                SNEHABHI has been deployed! Visit @SNEHABHI_UPDATES for updates!!
            ----------------------------------------------------------------------
"""

# for channel plugins
plugin_channels = udB.get("PLUGIN_CHANNEL")

# Customize Ultroid Assistant...
snehabhi_bot.run_in_loop(customize())

# Load Addons from Plugin Channels.
if plugin_channels:
    snehabhi_bot.run_in_loop(plug(plugin_channels))

# Send/Ignore Deploy Message..
if not udB.get("LOG_OFF"):
    snehabhi_bot.run_in_loop(ready())

cleanup_cache()

if __name__ == "__main__":
    LOGS.info(
        f"Took {time_formatter((time.time() - start_time)*1000)} to start •SNEHABHI•"
    )
    LOGS.info(suc_msg)
    snehabhi_bot.run()
