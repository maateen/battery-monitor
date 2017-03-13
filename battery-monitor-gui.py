import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.ApplicationWindow):
    """
    @description: This class displays the main window that the user will
    see when he wants to manage Battery Monitor
    """

    def __init__(self):
        Gtk.Window.__init__(self, title='Battery Monitor')
        self.set_default_size(800, 400)
        self.set_resizable(True)
        self.set_border_width(0)
        self.get_focus()
        self.set_position(Gtk.WindowPosition.CENTER)
        path = os.path.dirname(os.path.abspath(__file__))
        self.set_default_icon_from_file(os.path.join(path, 'icons/icon.png'))

        # class variable
        self.config_dir = os.path.expanduser('~/.config/battery-monitor')
        self.config_file = os.path.join(self.config_dir, 'battery-monitor.txt')
        self.very_low_battery = '10'
        self.low_battery = '30'
        self.first_custom_warning = ''
        self.second_custom_warning = ''
        self.third_custom_warning = ''
        self.battery_checking_interval = '3'
        self.notification_stability = '5'
        self.load_config()

        label0 = Gtk.Label('Very Low Battery Warning at')
        label0.set_justify(Gtk.Justification.LEFT)
        label0.set_halign(Gtk.Align.START)
        label0.set_hexpand(True)
        label1 = Gtk.Label('Low Battery Warning at')
        label1.set_justify(Gtk.Justification.LEFT)
        label1.set_halign(Gtk.Align.START)
        label1.set_hexpand(True)
        label2 = Gtk.Label('First Custom Warning at')
        label2.set_justify(Gtk.Justification.LEFT)
        label2.set_halign(Gtk.Align.START)
        label2.set_hexpand(True)
        label3 = Gtk.Label('Second Custom Warning at')
        label3.set_justify(Gtk.Justification.LEFT)
        label3.set_halign(Gtk.Align.START)
        label3.set_hexpand(True)
        label4 = Gtk.Label('Third Custom Warning at')
        label4.set_justify(Gtk.Justification.LEFT)
        label4.set_halign(Gtk.Align.START)
        label4.set_hexpand(True)
        label5 = Gtk.Label('Battery Checking Interval')
        label5.set_justify(Gtk.Justification.LEFT)
        label5.set_halign(Gtk.Align.START)
        label5.set_hexpand(True)
        label6 = Gtk.Label('Notification Stability')
        label6.set_justify(Gtk.Justification.LEFT)
        label6.set_halign(Gtk.Align.START)
        label6.set_hexpand(True)

        self.entry0 = Gtk.Entry()
        self.entry0.set_text(str(self.very_low_battery))
        self.entry0.set_tooltip_text('Set in percentage')
        self.entry1 = Gtk.Entry()
        self.entry1.set_text(str(self.low_battery))
        self.entry1.set_tooltip_text('Set in percentage')
        self.entry2 = Gtk.Entry()
        self.entry2.set_text(str(self.first_custom_warning))
        self.entry2.set_tooltip_text('Set in percentage')
        self.entry3 = Gtk.Entry()
        self.entry3.set_text(str(self.second_custom_warning))
        self.entry3.set_tooltip_text('Set in percentage')
        self.entry4 = Gtk.Entry()
        self.entry4.set_text(str(self.third_custom_warning))
        self.entry4.set_tooltip_text('Set in percentage')
        self.entry5 = Gtk.Entry()
        self.entry5.set_text(str(self.battery_checking_interval))
        self.entry5.set_tooltip_text('Set in second')
        self.entry6 = Gtk.Entry()
        self.entry6.set_text(str(self.notification_stability))
        self.entry6.set_tooltip_text('Set in second')

        save_button = Gtk.Button(label='Save')
        save_button.connect('clicked', self.save_config)

        grid = Gtk.Grid()
        self.add(grid)
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
        grid.attach(self.entry6, 14, 6, 1, 1)
        grid.attach(save_button, 9, 7, 1, 1)

    def load_config(self):
        if os.path.exists(self.config_file):
            with open(self.config_file, 'r') as f:
                for line in f.readlines():
                    line = line.strip('\n')
                    field = line.split('=')
                    if field[0] == 'very_low_battery':
                        self.very_low_battery = field[1]
                    elif field[0] == 'low_battery':
                        self.low_battery = field[1]
                    elif field[0] == 'first_custom_warning':
                        self.first_custom_warning = field[1]
                    elif field[0] == 'second_custom_warning':
                        self.second_custom_warning = field[1]
                    elif field[0] == 'third_custom_warning':
                        self.third_custom_warning = field[1]
                    elif field[0] == 'battery_checking_interval':
                        self.battery_checking_interval = field[1]
                    elif field[0] == 'notification_stability':
                        self.notification_stability = field[1]
        else:
            print('Config file is missing.')

    def save_config(self, widget):
        if os.path.exists(self.config_dir):
            pass
        else:
            os.makedirs(self.config_dir)
        with open(self.config_file, 'w') as f:
            f.write('very_low_battery=' + self.entry0.get_text() + '\n')
            f.write('low_battery=' + self.entry1.get_text() + '\n')
            f.write('first_custom_warning=' + self.entry2.get_text() + '\n')
            f.write('second_custom_warning=' + self.entry3.get_text() + '\n')
            f.write('third_custom_warning=' + self.entry4.get_text() + '\n')
            f.write('battery_checking_interval=' +
                    self.entry5.get_text() + '\n')
            f.write('notification_stability=' + self.entry6.get_text() + '\n')
            f.close()
            dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                       Gtk.ButtonsType.OK,
                                       "Successfully Saved!")
            dialog.format_secondary_text(
                'You settings have been saved successfully.')
            dialog.run()
            print("Info dialog closed")
            dialog.destroy()

win = MainWindow()
win.connect('delete_event', Gtk.main_quit)
win.show_all()
Gtk.main()
