#!/usr/bin/env python3

# standard library
import subprocess
import sys
import time

# imports from current project
from BatteryMonitor import BatteryMonitor
from Notification import Notification


def main() -> None:
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

if __name__ == '__main__':
    main()
