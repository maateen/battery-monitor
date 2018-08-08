#!/usr/bin/env python3

# standard library
import configparser
import os

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# imports from current project
from .config import CONFIG_FILE
from .config import ICONS
from .ErrorLib import ValidationError



class SettingsWindow(Gtk.Window):
    """GUI class for Settings Window.

    This class displays the Settings window in where the user can manage the configurations for Battery Monitor.
    """

    def __init__(self):
        Gtk.Window.__init__(self, title='Battery Monitor')
        self.set_default_size(800, 400)
        self.set_resizable(True)
        self.set_border_width(0)
        self.get_focus()
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_default_icon_from_file(ICONS['app'])
        self.config_dir = os.path.dirname(CONFIG_FILE)
        self.config = configparser.ConfigParser()
        self.__load_config()

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)
        self.notebook.append_page(self.__configuration_page(), Gtk.Label('Configuration'))

    def __configuration_page(self):
        label0 = Gtk.Label('Critical Battery Warning at')
        label0.set_justify(Gtk.Justification.LEFT)
        label0.set_halign(Gtk.Align.START)
        label0.set_hexpand(True)
        label1 = Gtk.Label('Low Battery Warning at')
        label1.set_justify(Gtk.Justification.LEFT)
        label1.set_halign(Gtk.Align.START)
        label1.set_hexpand(True)
        label2 = Gtk.Label('Third Custom Warning at')
        label2.set_justify(Gtk.Justification.LEFT)
        label2.set_halign(Gtk.Align.START)
        label2.set_hexpand(True)
        label3 = Gtk.Label('Second Custom Warning at')
        label3.set_justify(Gtk.Justification.LEFT)
        label3.set_halign(Gtk.Align.START)
        label3.set_hexpand(True)
        label4 = Gtk.Label('First Custom Warning at')
        label4.set_justify(Gtk.Justification.LEFT)
        label4.set_halign(Gtk.Align.START)
        label4.set_hexpand(True)
        label5 = Gtk.Label('Notification Stability Time')
        label5.set_justify(Gtk.Justification.LEFT)
        label5.set_halign(Gtk.Align.START)
        label5.set_hexpand(True)

        self.entry0 = Gtk.Entry()
        self.entry0.set_text(str(self.critical_battery))
        self.entry0.set_tooltip_text('Set in percentage')
        self.entry1 = Gtk.Entry()
        self.entry1.set_text(str(self.low_battery))
        self.entry1.set_tooltip_text('Set in percentage')
        self.entry2 = Gtk.Entry()
        self.entry2.set_text(str(self.third_custom_warning))
        self.entry2.set_tooltip_text('Set in percentage, must be smaller than Other Warnings')
        self.entry3 = Gtk.Entry()
        self.entry3.set_text(str(self.second_custom_warning))
        self.entry3.set_tooltip_text('Set in percentage, , must be greater than Third Custom Warning')
        self.entry4 = Gtk.Entry()
        self.entry4.set_text(str(self.first_custom_warning))
        self.entry4.set_tooltip_text('Set in percentage, must be greater than Second Custom Warning')
        self.entry5 = Gtk.Entry()
        self.entry5.set_text(str(self.notification_stability))
        self.entry5.set_tooltip_text('Set in second')

        save_button = Gtk.Button(label='Save')
        save_button.connect('clicked', self.__save_config)

        grid = Gtk.Grid()
        grid.set_row_spacing(15)
        grid.set_hexpand(True)
        grid.set_vexpand(True)
        grid.set_border_width(10)
        grid.set_column_spacing(2)
        grid.set_column_homogeneous(False)
        grid.attach(label0, 0, 0, 14, 1)
        grid.attach(self.entry0, 14, 0, 1, 1)
        grid.attach(label1, 0, 1, 14, 1)
        grid.attach(self.entry1, 14, 1, 1, 1)
        grid.attach(label2, 0, 2, 14, 1)
        grid.attach(self.entry2, 14, 2, 1, 1)
        grid.attach(label3, 0, 3, 14, 1)
        grid.attach(self.entry3, 14, 3, 1, 1)
        grid.attach(label4, 0, 4, 14, 1)
        grid.attach(self.entry4, 14, 4, 1, 1)
        grid.attach(label5, 0, 5, 14, 1)
        grid.attach(self.entry5, 14, 5, 1, 1)
        grid.attach(save_button, 9, 7, 1, 1)

        return grid

    def __load_config(self):
        """Loads configurations from config file.

        Tries to read and parse from config file. If the config file is missing or not readable, then it triggers default configurations.
        """

        try:
            self.config.read(CONFIG_FILE)
            self.critical_battery = self.config['settings']['critical_battery']
            self.low_battery = self.config['settings']['low_battery']
            self.first_custom_warning = self.config['settings']['first_custom_warning']
            self.second_custom_warning = self.config['settings']['second_custom_warning']
            self.third_custom_warning = self.config['settings']['third_custom_warning']
            self.notification_stability = self.config['settings']['notification_stability']
        except:
            print('Config file is missing or not readable. Using default configurations.')
            self.critical_battery = '10'
            self.low_battery = '30'
            self.first_custom_warning = ''
            self.second_custom_warning = ''
            self.third_custom_warning = ''
            self.notification_stability = '5'

    def __save_config(self, widget):
        """Saves configurations to config file.

        Saves user-defined configurations to config file. If the config file does not exist, it creates a new config file (~/.config/battery-monitor/battery-monitor.cfg) in user's home directory.
        """

        if os.path.exists(self.config_dir):
            pass
        else:
            os.makedirs(self.config_dir)

        self.config['settings'] = {
            'critical_battery': self.entry0.get_text(),
            'low_battery': self.entry1.get_text(),
            'third_custom_warning': self.entry2.get_text(),
            'second_custom_warning': self.entry3.get_text(),
            'first_custom_warning': self.entry4.get_text(),
            'notification_stability': self.entry5.get_text()
        }

        try:
            self.__validate_config(self.config['settings'])
            with open(CONFIG_FILE, 'w') as f:
                self.config.write(f)
                dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, 'Successfully Saved!')
                dialog.format_secondary_text(
                    'You settings have been saved successfully.')
                response = dialog.run()
                if response == Gtk.ResponseType.OK:
                    self.close()
                dialog.destroy()
        except ValidationError as message:
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, 'Validation Error!')
            dialog.format_secondary_text(str(message))
            dialog.run()
            dialog.destroy()

    def __validate_config(self, config):
        """validates config before saving to config file."""

        if bool(config['critical_battery']) and bool(config['low_battery']):
            if int(config['critical_battery']) >= int(config['low_battery']):
                raise ValidationError('The value of low battery warning must be greater than the value of critical battery warning.')
        else:
            if bool(config['critical_battery']):
                raise ValidationError('Low battery warning can not be empty.')
            else:
                raise ValidationError('Critical battery warning can not be empty.')

        if bool(config['low_battery']) and bool(config['third_custom_warning']):
            if int(config['low_battery']) >= int(config['third_custom_warning']):
                raise ValidationError('The value of third custom warning must be greater than the value of low battery warning.')

        if bool(config['third_custom_warning']) and bool(config['second_custom_warning']):
            if int(config['third_custom_warning']) >= int(config['second_custom_warning']):
                raise ValidationError('The value of second custom warning must be greater than the value 0f third custom warning.')

        if bool(config['second_custom_warning']) and bool(config['first_custom_warning']):
            if int(config['second_custom_warning']) >= int(config['first_custom_warning']):
                raise ValidationError('The value of first custom warning must be greater than then value of second custom warning.')

        if bool(config['notification_stability']):
            if int(config['notification_stability']) <= 0:
                raise ValidationError('Notification stability time must be greater than zero.')
        else:
            raise ValidationError('Notification stability time can not be empty.')
