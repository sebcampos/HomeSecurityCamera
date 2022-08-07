# This module is only to be used if there is a pijuice battery installed #

import pijuice
pj = pijuice.PiJuice(1, 0x14)

def get_charge_level() -> int:
    """
    This method calls the pijuice get chargelevel method
    and returns the value as an integer
    """
    return pj.status.GetChargeLevel()["data"]

def check_charge_level() -> str:
    """
    This method gets the charge level
    from the pijuice method and yields a formated
    string depending on the charge level
    :return: string representation of battery level
    """
    battery_level = int(get_charge_level())
    if battery_level <= 75 and battery_level > 50:
        return f"[BATTERY BELOW 75] {battery_level}%"

    if battery_level <= 50 and battery_level > 25:
        return f"[BATTERY BELOW 50] {battery_level}%"

    if battery_level <= 25 and battery_level >15:
        return f"[ WARNING BATTERY BELOW 25] {battery_level}%"

    else:
        return  f"[BATTERY] {battery_level}%"
