#!/usr/bin/env python3

import os
import subprocess
import sys
import time
import random
import configparser

import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify

from config import ICONS, MESSAGES

class BatteryMonitor:
    raw_battery_info = ''
    processed_battery_info = {}

    def __init__(self, TEST_MODE):
        self.TEST_MODE = TEST_MODE
        self.raw_battery_info = self.get_raw_battery_info()
        self.get_processed_battery_info()

    def get_raw_battery_info(self):
        if self.TEST_MODE:
            state = random.choice(['Charging', 'Discharging'])
            percentage = str(random.randint(0, 100))
            remaining = random.choice(['03:24:25 remaining', 'discharging at zero rate - will never fully discharge'])
            result = "Battery 0: " + state + ", " + percentage + "%, " + remaining
            print(result)
            return result.encode('UTF-8')
        else:
            command = "acpi -b"
            raw_info = subprocess.check_output(command,
                                            stderr=subprocess.PIPE,
                                            shell=True)
        return raw_info

    def is_updated(self):
        current_raw_info = self.get_raw_battery_info()

        if self.raw_battery_info != current_raw_info:
            self.raw_battery_info = current_raw_info
            return True

        return False

    def get_processed_battery_info(self):
        in_list = (self.raw_battery_info.decode("utf-8", "strict").lower().strip('\n')
                   .split(": ", 1)[1].split(", "))

        self.processed_battery_info["state"] = in_list[0]
        self.processed_battery_info["percentage"] = in_list[1]
        try:
            self.processed_battery_info["remaining"] = in_list[2]
        except IndexError:
            pass

        return self.processed_battery_info


class Notification:
    last_notification = None
    last_percentage = None

    def __init__(self, type):
        Notify.init("Battery Monitor")
        message = MESSAGES[type]
        head = message[0]
        body = message[1]
        icon = ICONS[type]
        self.notifier = Notify.Notification.new(head, body, icon)
        self.notifier.set_urgency(Notify.Urgency.CRITICAL)
        self.notifier.show()

        # class variable
        self.config_dir = os.path.expanduser('~/.config/battery-monitor')
        self.config_file = os.path.join(self.config_dir, 'battery-monitor.txt')
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

    def show_notification(self, type, battery_percentage,
                          remaining_time=None, _time=5):

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


try:
    print("Press 'ctrl+C' to exit.")

    # checking Test Mode enabled or not
    try:
        if sys.argv[1] == '--test':
            TEST_MODE = True
        else:
            TEST_MODE = False
    except IndexError:
        TEST_MODE = False

    monitor = BatteryMonitor(TEST_MODE)
    notification = Notification("success")
    time.sleep(3)
    notification.show_specific_notifications(monitor)

    while True:
        if monitor.is_updated():
            notification.show_specific_notifications(monitor)

        time.sleep(3)

except KeyboardInterrupt:
    print("\nBattery Monitor has been exited successfully.")
    del notification
    sys.exit(0)

except subprocess.CalledProcessError:
    notification = Notification("fail")
    del notification
