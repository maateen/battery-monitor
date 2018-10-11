#!/usr/bin/env python3

# standard library
import os
import configparser

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# imports from current project
from ErrorLib import ValidationError
from config import APP_ICON_NAMES
from config import CONFIG_FILE
from config import ICON_PATH

class UserConfig:

    @staticmethod
    def load_config(fill_with_preset_values=False):
        """Loads configurations from config file.

        Tries to read and parse from config file. If the config file is missing, not readable or values can't be parsed as ints (except icon), then it triggers default configurations.
        """

        config = configparser.ConfigParser()
        try:
            config.read(CONFIG_FILE)
            user_config = {'critical_battery':  int(config['settings']['critical_battery']),
                           'low_battery': int(config['settings']['low_battery']),
                           'first_custom_warning': int(config['settings']['first_custom_warning']),
                           'second_custom_warning': int(config['settings']['second_custom_warning']),
                           'third_custom_warning': int(config['settings']['third_custom_warning']),
                           'notification_stability': int(config['settings']['notification_stability']),
                           'icon': config['settings']['icon']}
        except (KeyError, ValueError) as E:
            print('Config file is missing, not readable, or (a) value(s) was / were invalid. Using default configurations')
            user_config = {'critical_battery': 10,
                           'low_battery': 30,
                           'first_custom_warning': 0,
                           'second_custom_warning': 0,
                           'third_custom_warning': 0,
                           'notification_stability': 5,
                           'icon': APP_ICON_NAMES[0]}

        if user_config['icon'] not in APP_ICON_NAMES:
            print('App icon specified in config file isn\'t valid. Using default icon.')
            user_config['icon'] = APP_ICON_NAMES[0]

        return user_config

    @staticmethod
    def save(user_config, settings_window):
        """Saves configurations to config file.

        Saves user-defined configurations to config file. If the config file does not exist, it creates a new config file (~/.config/battery-monitor/battery-monitor.cfg) in user's home directory.
        """

        config_dir = os.path.dirname(CONFIG_FILE)
        config = configparser.ConfigParser()

        if os.path.exists(config_dir) is not True:
            os.makedirs(config_dir)

        try:
            UserConfig.validate(user_config)
        except ValidationError as message:
            UserConfig.show_validation_error_dialog(message, settings_window)
            return

        config['settings'] = user_config
        with open(CONFIG_FILE, 'w') as f:
            config.write(f)
            dialog = Gtk.MessageDialog(settings_window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, 'Successfully Saved!')
            dialog.format_secondary_text(
                'You settings have been saved successfully.')
            response = dialog.run()
            if response == Gtk.ResponseType.OK:
                settings_window.close()
            dialog.destroy()

    @staticmethod
    def show_validation_error_dialog(validation_error, window):
        """show gtk dialog, alerting the user that a validation error occurred
        """

        dialog = Gtk.MessageDialog(window, 0, Gtk.MessageType.ERROR, Gtk.ButtonsType.CANCEL, 'Validation Error!')
        dialog.format_secondary_text(str(validation_error))
        dialog.run()
        dialog.destroy()

    @staticmethod
    def validate(user_config):
        """validates config.
        """

        if bool(user_config['critical_battery']) and bool(user_config['low_battery']):
            if user_config['critical_battery'] >= user_config['low_battery']:
                raise ValidationError(
                    'The value of low battery warning must be greater than the value of critical battery warning.')
        else:
            if bool(user_config['critical_battery']):
                raise ValidationError('Low battery warning can not be empty.')
            else:
                raise ValidationError('Critical battery warning can not be empty.')
        if bool(user_config['low_battery']) and bool(user_config['third_custom_warning']):
            if user_config['low_battery'] >= user_config['third_custom_warning']:
                raise ValidationError(
                    'The value of third custom warning must be greater than the value of low battery warning.')

        if bool(user_config['third_custom_warning']) and bool(user_config['second_custom_warning']):
            if user_config['third_custom_warning'] >= user_config['second_custom_warning']:
                raise ValidationError(
                    'The value of second custom warning must be greater than the value 0f third custom warning.')

        if bool(user_config['second_custom_warning']) and bool(user_config['first_custom_warning']):
            if user_config['second_custom_warning'] >= user_config['first_custom_warning']:
                raise ValidationError(
                    'The value of first custom warning must be greater than the value of second custom warning.')

        if bool(user_config['notification_stability']):
            if user_config['notification_stability'] <= 0:
                raise ValidationError('Notification stability time must be greater than zero.')
        else:
            raise ValidationError('Notification stability time can not be empty.')

        if os.path.isfile(ICON_PATH + user_config['icon'].replace(' ', '-').lower() + '.png') is not True:
            raise ValidationError('The icon you selected is not available. Please choose another icon.')