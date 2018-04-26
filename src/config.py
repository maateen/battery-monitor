#!/usr/bin/env python3

import os

_path = os.path.dirname(os.path.abspath(__file__))
_icon_path = _path + '/icons/'

CONFIG_FILE = '~/.config/battery-monitor/battery-monitor.cfg'

ICONS = {
    "app": "icon.png",
    "success": "icon.png",
    "fail": "icon.png",
    "charging": "charging.png",
    "discharging": "discharging.png",
    "full":  "not-charging.png",
    "unknown":  "not-charging.png",
    "low_battery": "low-battery.png",
    "critical_battery": "critical-battery.png",
    "first_custom_warning": "discharging.png",
    "second_custom_warning": "discharging.png",
    "third_custom_warning": "discharging.png",
}

for key in ICONS:
	ICONS[key] = _icon_path + ICONS[key]

MESSAGES = {
    "success": (
        u"Battery Monitor",
        u"Congrats! Started to monitor just now."
    ),

    "fail": (
        u"Battery Monitor",
        u"Battery is not yet present!"
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

    "critical_battery": (
        u"Critically Low Battery",
        u"Only {battery_percentage} %, {remaining_time}"
    ),

    "low_battery": (
        u"Low Battery",
        u"Now {battery_percentage} %, {remaining_time}"
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
