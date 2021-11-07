from .. import *

CMD_HELP = {}
# ----------------------------------------------#


def sudoers():
    from .. import udB

    if udB.get("SUDOS"):
        return udB["SUDOS"].split()
    return []


def should_allow_sudo():
    from .. import udB

    return udB.get("SUDO") == "True"


def owner_and_sudos(castint=False):
    from .. import udB, snehabhi_bot

    data = [str(snehabhi_bot.uid), *sudoers()]
    if castint:
        return [int(a) for a in data]
    return data


# ------------------------------------------------ #


def append_or_update(load, func, name, arggs):
    if isinstance(load, list):
        return load.append(func)
    if isinstance(load, dict):
        if load.get(name):
            return load[name].append((func, arggs))
        return load.update({name: [(func, arggs)]})
