import os

_path = os.path.dirname(os.path.abspath(__file__))
_icon_path = _path + '/icons/'

ICONS = {
    "success": "icon.png",
    "fail": "icon.png",
    "Charging": "charging.png",
    "Discharging": "discharging.png",
    "Full":  "not-charging.png",
    "Unknown":  "not-charging.png",
    "very_low_battery": "low-battery.png",
    "low_battery": "low-battery.png",
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

    "Charging": (
        u"Charging",
        u"Now {battery_percentage} %, {remaining_time}"
    ),
    
    "Discharging": (
        u"Discharging",
        u"Now {battery_percentage} %, {remaining_time}"
    ),
    
    "Full": (
        u"Fully Charged",
        u"{battery_percentage} % Remaining"
    ),

    "Unknown": (
        u"Fully Charged",
        u"{battery_percentage} % Remaining"
    ),

    "very_low_battery": (
        u"Critically Low Battery",
        u"Only {battery_percentage} %, {remaining_time}"
    ),

    "low_battery": (
        u"Low Battery",
        u"Now {battery_percentage} %, {remaining_time}"
    ),
}

