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
from AboutWindow import AboutWindow
from BatteryMonitor import BatteryMonitor
from Notification import Notification
from SettingsWindow import SettingsWindow

class AppIndicator:
    """Class for system tray icon.

    This class will show Battery Monitor icon in system tray.
    """

    TEST_MODE: bool

    def __init__(self, TEST_MODE: bool = False):
        self.indicator = AppIndicator3.Indicator.new(APPINDICATOR_ID, ICONS['app'], AppIndicator3.IndicatorCategory.SYSTEM_SERVICES)
        self.indicator.set_title('Battery Monitor')
        self.indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

        # create menu
        self.indicator.set_menu(self.__create_menu())

        # run the daemon
        self.daemon = Thread(target=self.__run_daemon, args=(TEST_MODE,))
        self.daemon.setDaemon(True)
        self.daemon.start()

    def __about_window(self, *args):
        about_window = AboutWindow()
        about_window.show()

    def __create_menu(self):
        menu = Gtk.Menu()

        item_settings = Gtk.MenuItem('Settings')
        item_settings.connect("activate", self.__settings_window)
        menu.append(item_settings)

        item_about = Gtk.MenuItem('About')
        item_about.connect("activate", self.__about_window)
        menu.append(item_about)

        item_quit = Gtk.MenuItem('Quit')
        item_quit.connect("activate", self.__quit)
        menu.append(item_quit)
        menu.show_all()

        return menu

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

    def __settings_window(self, *args):
        settings = SettingsWindow()
        settings.connect('destroy', Gtk.main_quit)
        settings.show_all()
        Gtk.main()

    def __quit(self, *args):
        Gtk.main_quit()
