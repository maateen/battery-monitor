#!/usr/bin/env python3

# standard library
import configparser
import os
import time

# third-party library
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

# imports from current project
from config import ICONS
from config import MESSAGES



class Notification:
    """Triggers notification on battery state changes.

    Triggers informative and effective notification on every change of battery state.
    """

    last_notification: str
    last_percentage: int

    def __init__(self, type: str) -> None:
        Notify.init("Battery Monitor")
        message = MESSAGES[type]
        head = message[0]
        body = message[1]
        icon = ICONS[type]
        self.last_notification = ''
        self.last_percentage = 0
        self.notifier = Notify.Notification.new(head, body, icon)
        self.notifier.set_urgency(Notify.Urgency.CRITICAL)
        self.notifier.show()

        # class variable
        self.config_dir = os.path.expanduser('~/.config/battery-monitor')
        self.config_file = os.path.join(self.config_dir, 'battery-monitor.cfg')
        self.config = configparser.ConfigParser()
        self.load_config()

    def load_config(self):
        try:
            self.config.read(self.config_file)
            try:
                self.very_low_battery = int(self.config['settings']['very_low_battery'])
            except ValueError:
                self.very_low_battery = 10
            try:
                self.low_battery = int(self.config['settings']['low_battery'])
            except ValueError:
                self.low_battery = 30
            try:
                self.first_custom_warning = int(self.config['settings']['first_custom_warning'])
            except ValueError:
                self.first_custom_warning = -1
            try:
                self.second_custom_warning = int(self.config['settings']['second_custom_warning'])
            except ValueError:
                self.second_custom_warning = -2
            try:
                self.third_custom_warning = int(self.config['settings']['third_custom_warning'])
            except ValueError:
                self.third_custom_warning = -3
            try:
                self.notification_stability = int(self.config['settings']['notification_stability'])
            except ValueError:
                self.notification_stability = 5
        except:
            print('Config file is missing or not readable. Using defaults!')
            self.very_low_battery = 10
            self.low_battery = 30
            self.first_custom_warning = -1
            self.second_custom_warning = -2
            self.third_custom_warning = -3
            self.notification_stability = 5

    def show_notification(self, type: str, battery_percentage: int,
                          remaining_time: str = None, _time: int = 5) -> None:

        message = MESSAGES[type]
        head = message[0]
        body = message[1].format(battery_percentage=battery_percentage,
                                 remaining_time=remaining_time)
        icon = ICONS[type]
        self.notifier.update(head, body, icon)
        self.notifier.show()
        time.sleep(self.notification_stability)
        self.notifier.close()

    def show_specific_notifications(self, monitor):
        info = monitor.get_processed_battery_info()
        state = info["state"]
        percentage = int(info["percentage"].replace("%", ""))
        remaining = info.get("remaining")

        # Show warning one time for each percentage while its low battery.
        # Low battery notification shuld not be show while it is charging.
        # Also Keep in memory which notification was showed last time
        if self.last_percentage != percentage and state != "charging":
            self.last_percentage = percentage
            if percentage <= self.very_low_battery:
                self.last_notification = "very_low_battery"
                self.show_notification(type="very_low_battery",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "very_low_battery"

            elif percentage <= self.low_battery:
                self.last_notification = "low_battery"
                self.show_notification(type="low_battery",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "low_battery"

            elif percentage <= self.first_custom_warning:
                self.last_notification = "first_custom_warning"
                self.show_notification(type="first_custom_warning",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "first_custom_warning"

            elif percentage <= self.second_custom_warning:
                self.last_notification = "second_custom_warning"
                self.show_notification(type="second_custom_warning",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "second_custom_warning"

            elif percentage <= self.third_custom_warning:
                self.last_notification = "third_custom_warning"
                self.show_notification(type="third_custom_warning",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "third_custom_warning"

        # Show Notification only while state changes.
        # Notification should not be shown for each percentage change.
        # Sometime acpi return remaining time like
        # *discharging at zero rate - will never fully discharge*
        # We should skip it
        if state != self.last_notification and remaining != "discharging at zero rate - will never fully discharge":
            self.last_notification = state
            self.show_notification(type=state,
                                   battery_percentage=percentage,
                                   remaining_time=remaining)

            return state

    def __del__(self):
        self.notifier.close()
        Notify.uninit()
