#!/usr/bin/env python3

# standard library
import configparser
import time

# third-party library
import gi
from gi.repository import GLib
gi.require_version('Notify', '0.7')
from gi.repository import Notify

# imports from current project
from BatteryMonitor import BatteryMonitor
from config import CONFIG_FILE
from config import ICONS
from config import MESSAGES
from UserConfig import UserConfig




class Notification:
    """Triggers notification on battery state changes.

    Triggers informative and effective notification on every change of battery state.
    """

    last_notification: str
    last_percentage: int

    def __init__(self, type: str) -> None:
        # initiating notification
        Notify.init("Battery Monitor")
        message = MESSAGES[type]
        head = message[0]
        body = message[1]
        icon = ICONS[type]
        self.last_percentage = 0
        self.last_notification = ''
        self.notifier = Notify.Notification.new(head, body, icon)
        self.notifier.set_urgency(Notify.Urgency.CRITICAL)
        try:
            self.notifier.show()
        except GLib.GError as e:
            # fixing GLib.GError: g-dbus-error-quark blindly
            pass
        self.config = configparser.ConfigParser()
        self.user_config = UserConfig.load_config()

    def load_config(self):
        try:
            self.config.read(CONFIG_FILE)
            try:
                self.critical_battery = int(self.config['settings']['critical_battery'])
            except ValueError:
                self.critical_battery = 10
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
            print('Config file is missing or not readable. Using default configurations.')
            self.critical_battery = 10
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
        try:
            self.notifier.show()
        except GLib.GError as e:
            # fixing GLib.GError: g-dbus-error-quark blindly
            # To Do: investigate the main reason and make a fix
            pass
        time.sleep(self.user_config['notification_stability'])
        self.notifier.close()

    def show_specific_notifications(self, monitor: BatteryMonitor):
        """Shows specific notifications depending on the changes of battery state.

        Shows Notification only while state or last notification changes. Notification will not be shown for each percentage change. Sometimes acpi returns remaining time like *discharging at zero rate - will never fully discharge* We will skip it.
        """
        info = monitor.get_processed_battery_info()
        state = info["state"]
        percentage = int(info["percentage"].replace("%", ""))
        remaining = info.get("remaining")

        if state == 'discharging':
            if (percentage != self.last_percentage and
                    remaining != "discharging at zero rate - will never fully discharge"):
                self.last_percentage = percentage
                if percentage <= self.user_config['critical_battery']:
                    self.last_notification = "critical_battery"
                    self.show_notification(type="critical_battery",
                                           battery_percentage=percentage,
                                           remaining_time=remaining)

                    return "critical_battery"

                elif (percentage <= self.user_config['low_battery'] and
                      self.last_notification != "low_battery"):
                    self.last_notification = "low_battery"
                    self.show_notification(type="low_battery",
                                           battery_percentage=percentage,
                                           remaining_time=remaining)

                    return "low_battery"

                elif (percentage <= self.user_config['third_custom_warning'] and
                      self.last_notification != "third_custom_warning"):
                    self.last_notification = "third_custom_warning"
                    self.show_notification(type="third_custom_warning",
                                           battery_percentage=percentage,
                                           remaining_time=remaining)

                    return "third_custom_warning"

                elif (percentage <= self.user_config['second_custom_warning'] and
                      self.last_notification != "second_custom_warning"):
                    self.last_notification = "second_custom_warning"
                    self.show_notification(type="second_custom_warning",
                                           battery_percentage=percentage,
                                           remaining_time=remaining)

                    return "second_custom_warning"

                elif (percentage <= self.user_config['first_custom_warning'] and
                      self.last_notification != "first_custom_warning"):
                    self.last_notification = "first_custom_warning"
                    self.show_notification(type="first_custom_warning",
                                           battery_percentage=percentage,
                                           remaining_time=remaining)

                    return "first_custom_warning"
        else:
            if (state != self.last_notification and
                    remaining != "discharging at zero rate - will never fully discharge"):
                self.last_notification = state
                self.show_notification(type=state,
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return state

    def __del__(self):
        self.notifier.close()
        Notify.uninit()
