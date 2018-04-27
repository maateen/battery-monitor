#!/usr/bin/env python3

# standard library
import signal
import subprocess
import sys
import time

# imports from current project
from BatteryMonitor import BatteryMonitor
from Notification import Notification


def main() -> None:
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    # checking Test Mode enabled or not
    try:
        if sys.argv[1] == '--test':
            TEST_MODE = True
        else:
            TEST_MODE = False
    except IndexError:
        TEST_MODE = False

    try:
        monitor = BatteryMonitor(TEST_MODE)
    except subprocess.CalledProcessError as e:
        notification = Notification("acpi")
        time.sleep(3)
        del notification
        sys.exit(1)

    notification = Notification("success")
    time.sleep(3)
    notification.show_specific_notifications(monitor)

    while True:
        if monitor.is_updated():
            notification.show_specific_notifications(monitor)
        time.sleep(3)

if __name__ == '__main__':
    main()
