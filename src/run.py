#!/usr/bin/env python3

# standard library
import signal
import sys

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GObject

# imports from current project
from AppIndicator import AppIndicator


def main() -> None:
    # checking Test Mode enabled or not
    try:
        if sys.argv[1] == '--test':
            TEST_MODE = True
        else:
            TEST_MODE = False
    except IndexError:
        TEST_MODE = False

    # initiaing app indicator
    indicator = AppIndicator(TEST_MODE)
    GObject.threads_init()
    Gtk.main()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    main()
