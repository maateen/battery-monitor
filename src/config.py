#!/usr/bin/env python3

# standard library
import os

_path = os.path.dirname(os.path.abspath(__file__))
ICON_PATH = _path + '/icons/'

APP_ICON_NAMES = ["Default Icon", "Light Icon", "Dark Icon"]

APPINDICATOR_ID = 'batterymonitor'

CONFIG_FILE = os.path.expanduser('~/.config/battery-monitor/battery-monitor.cfg')

ICONS = {
    "success": "default-icon.png",
    "fail": "default-icon.png",
    "acpi": "default-icon.png",
    "charging": "charging.png",
    "discharging": "discharging.png",
    "full":  "full-charge.png",
    "unknown":  "not-charging.png",
    "low_battery": "low-battery.png",
    "critical_battery": "critical-battery.png",
    "first_custom_warning": "discharging.png",
    "second_custom_warning": "discharging.png",
    "third_custom_warning": "discharging.png"
}

for key in ICONS:
    ICONS[key] = ICON_PATH + ICONS[key]

ICONS["app"] = []

for icon_index in range(len(APP_ICON_NAMES)):
    ICONS["app"].append(ICON_PATH + APP_ICON_NAMES[icon_index].replace(" ", "-").lower() + ".png")

MESSAGES = {
    "success": (
        u"Battery Monitor",
        u"Cheers! Your battery is being monitored now."
    ),

    "fail": (
        u"Battery Monitor",
        u"Alas! Battery is not yet present!"
    ),

    "acpi": (
        u"Battery Monitor",
        u"Dependency Error! acpi is not installed.",
    ),

    "charging": (
        u"Charging",
        u"Now {battery_percentage} %, {remaining_time}"
    ),

    "discharging": (
        u"Discharging",
        u"Now {battery_percentage} %, {remaining_time}"
    ),

    "full": (
        u"Fully Charged",
        u"{battery_percentage} % Remaining"
    ),

    "unknown": (
        u"Fully Charged",
        u"{battery_percentage} % Remaining"
    ),

    "low_battery": (
        u"Low Battery",
        u"Now {battery_percentage} %, {remaining_time}"
    ),

    "critical_battery": (
        u"Critically Low Battery",
        u"Only {battery_percentage} %, {remaining_time}"
    ),

    "first_custom_warning": (
        u"First Custom Warning",
        u"Now {battery_percentage} %, {remaining_time}"
    ),

    "second_custom_warning": (
        u"Second Custom Warning",
        u"Now {battery_percentage} %, {remaining_time}"
    ),

    "third_custom_warning": (
        u"Third Custom Warning",
        u"Now {battery_percentage} %, {remaining_time}"
    ),
}

TEST_CASES = {
    "state": [
        "Full",
        "Charging",
        "Discharging",
    ],
    "remaining": [
        "00:10:12 remaining",
        "01:47:31 remaining",
        "02:33:47 remaining",
        "03:24:25 remaining",
        "discharging at zero rate - will never fully discharge",
    ],
}
