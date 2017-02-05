import subprocess
import sys
import time

import gi

gi.require_version('Notify', '0.7')
from gi.repository import Notify

try:
    # Python 3.x
    from .config import ICONS, MESSAGES
except:
    # Python 2.x
    from config import ICONS, MESSAGES


class BatteryMonitor:
    raw_battery_info = ''
    processed_battery_info = {}

    def __init__(self):
        self.raw_battery_info = self.get_raw_battery_info()
        self.get_processed_battery_info()

    def get_raw_battery_info(self):
        command = "acpi -b"
        raw_info = subprocess.check_output(command,
                                           stderr=subprocess.PIPE,
                                           shell=True)
        return raw_info

    def is_updated(self):
        current_raw_info = self.get_raw_battery_info()

        if self.raw_battery_info != current_raw_info:
            self.raw_battery_info = current_raw_info
            return False

        return True

    def get_processed_battery_info(self):
        in_list = (self.raw_battery_info.decode("utf-8", "strict")
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
        self.notifier = self.generate_notification(type)
        self.notifier.show()

    def generate_notification(self, type):
        # Generate a new notification and return a notifier object

        Notify.init("Battery Monitor")
        message = MESSAGES[type]
        head = message[0]
        body = message[1]
        icon = ICONS[type]
        notifier = Notify.Notification.new(head, body, icon)
        notifier.set_urgency(Notify.Urgency.CRITICAL)
        return notifier

    def show_notification(self, type, battery_percentage,
                          remaining_time=None, _time=5):

        message = MESSAGES[type]
        head = message[0]
        body = message[1].format(battery_percentage=battery_percentage,
                                 remaining_time=remaining_time)
        icon = ICONS[type]
        self.notifier.update(head, body, icon)
        self.notifier.show()
        time.sleep(_time)
        self.notifier.close()

    def show_specific_notifications(self, monitor):
        info = monitor.processed_battery_info
        state = info["state"]
        percentage = int(info["percentage"].replace("%", ""))
        remaining = info.get("remaining")

        # Show warning one time for each percentage while its low battery.
        # Low battery notification shuld not be show while it is charging.
        # Also Keep in memory which notification was showed last time
        if self.last_percentage != percentage and state != "charging":

            if percentage <= 10:
                self.last_notification = "very_low_battery"
                self.last_percentage = percentage
                self.show_notification(type="very_low_battery",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "very_low_battery"

            elif percentage == 30:
                self.last_notification = "low_battery"
                self.last_percentage = percentage
                self.show_notification(type="low_battery",
                                       battery_percentage=percentage,
                                       remaining_time=remaining)

                return "low_battery"

        # Show Notification only while state changes.
        # Notification should not be shown for each percentage change.
        # Sometime acpi return remaining time like 
        # *discharging at zero rate - will never fully discharge*
        # We should skip it
        if state != self.last_notification and remaining != "discharging at zero rate - will never fully discharge":
            self.last_notification = state
            self.last_percentage = percentage
            self.show_notification(type=state,
                                   battery_percentage=percentage,
                                   remaining_time=remaining)

            return state


try:
    print("Press 'ctrl+C' to exit.")

    monitor = BatteryMonitor()
    notification = Notification("success")
    time.sleep(3)
    notification.show_specific_notifications(monitor)

    while True:
        if not monitor.is_updated():
            monitor.get_processed_battery_info()
            notification.show_specific_notifications(monitor)

        time.sleep(3)

except KeyboardInterrupt:
    Notify.uninit()
    print("\nBattery Monitor has been exited successfully.")
    sys.exit(0)

except subprocess.CalledProcessError:
    # Means There are no battery
    notification = Notification("fail")
    Notify.uninit()
