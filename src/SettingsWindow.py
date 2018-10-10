#!/usr/bin/env python3

# standard library
import configparser
import os

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

# imports from current project
from config import CONFIG_FILE
from config import ICONS
from config import APP_ICON_NAMES
from UserConfig import UserConfig



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
        self.set_default_icon_from_file(ICONS['app'][0])
        self.config_dir = os.path.dirname(CONFIG_FILE)
        self.config = configparser.ConfigParser()
        self.user_config = UserConfig.load_config()

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
        label6 = Gtk.Label('Icon')
        label6.set_justify(Gtk.Justification.LEFT)
        label6.set_halign(Gtk.Align.START)
        label6.set_hexpand(True)

        self.entry0 = Gtk.Entry()
        self.entry0.set_text(str(self.user_config['critical_battery']))
        self.entry0.set_tooltip_text('Set in percentage')
        self.entry1 = Gtk.Entry()
        self.entry1.set_text(str(self.user_config['low_battery']))
        self.entry1.set_tooltip_text('Set in percentage')
        self.entry2 = Gtk.Entry()
        self.entry2.set_text(str(self.user_config['third_custom_warning']))
        self.entry2.set_tooltip_text('Set in percentage, must be smaller than Other Warnings')
        self.entry3 = Gtk.Entry()
        self.entry3.set_text(str(self.user_config['second_custom_warning']))
        self.entry3.set_tooltip_text('Set in percentage, , must be greater than Third Custom Warning')
        self.entry4 = Gtk.Entry()
        self.entry4.set_text(str(self.user_config['first_custom_warning']))
        self.entry4.set_tooltip_text('Set in percentage, must be greater than Second Custom Warning')
        self.entry5 = Gtk.Entry()
        self.entry5.set_text(str(self.user_config['notification_stability']))
        self.entry5.set_tooltip_text('Set in second')

        icon_store = Gtk.ListStore(str)
        
        for icon in APP_ICON_NAMES:
            icon_store.append([icon])

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
        self.icon_combo = Gtk.ComboBox.new_with_model(icon_store)
        
        renderer_text = Gtk.CellRendererText()
        self.icon_combo.pack_start(renderer_text, True)
        self.icon_combo.add_attribute(renderer_text, "text", 0)
        self.icon_combo.set_active(APP_ICON_NAMES.index(self.user_config['icon']))
        vbox.pack_start(self.icon_combo, False, False, True)
        
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
        grid.attach(label6, 0, 6, 14, 1)
        grid.attach(vbox, 14, 6, 1, 1)
        grid.attach(save_button, 9, 7, 1, 1)

        return grid

    def __save_config(self, widget):
        """ Writes all field into a dictionary and calls save_config() in UserConfig to save to file
        """
        try:
            user_config = {
                'critical_battery': int(self.entry0.get_text()),
                'low_battery': int(self.entry1.get_text()),
                'third_custom_warning': int(self.entry2.get_text()),
                'second_custom_warning': int(self.entry3.get_text()),
                'first_custom_warning': int(self.entry4.get_text()),
                'notification_stability': int(self.entry5.get_text()),
                'icon': APP_ICON_NAMES[self.icon_combo.get_active()]
            }
            UserConfig.save(user_config, self)
        except ValueError:
            UserConfig.show_validation_error_dialog('One or multiple fields contain values, which aren\'t valid', self)