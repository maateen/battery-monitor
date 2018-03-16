#!/usr/bin/env python3

# standard library
import configparser

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# imports from current project
from MainWindow import MainWindow


def main() -> None:
    win = MainWindow()
    win.connect('delete_event', Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == '__main__':
    main()
