#!/usr/bin/env python3

# standard library
import subprocess
import time
from threading import Thread

# third-party library
import gi
gi.require_version('AppIndicator3', '0.1')
from gi.repository import AppIndicator3
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# imports from current project
from config import APPINDICATOR_ID
from config import ICONS
from BatteryMonitor import BatteryMonitor
from Notification import Notification


class AppIndicator:
    """Class for system tray icon.

    This class will show Battery Monitor icon in system tray.
    """

    TEST_MODE: bool

    def __init__(self, TEST_MODE: bool = False):
        self.indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, ICONS['app'], AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        # create menu
        self.menu = Gtk.Menu()
        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect("activate", self.__quit)
        self.menu.append(item_quit)
        self.menu.show_all()
        self.indicator.set_menu(self.menu)

        # run the daemon
        self.daemon = Thread(target=self.__run_daemon, args=(TEST_MODE,))
        self.daemon.setDaemon(True)
        self.daemon.start()

    def __run_daemon(self, TEST_MODE: bool = False):
        # initiaing BatteryMonitor
        try:
            monitor = BatteryMonitor(TEST_MODE)
        except subprocess.CalledProcessError as e:
            # initiaing Notification
            notification = Notification("acpi")
            time.sleep(3)
            del notification
            self.__quit()

        # initiaing Notification
        notification = Notification("success")
        time.sleep(3)
        notification.show_specific_notifications(monitor)
        while True:
            if monitor.is_updated():
                notification.show_specific_notifications(monitor)
            time.sleep(3)

    def __quit(self, source=None):
        Gtk.main_quit()
