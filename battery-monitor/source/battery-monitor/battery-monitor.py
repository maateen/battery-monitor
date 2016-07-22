import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk
from gi.repository import Notify
import os, sys, subprocess


class MessageDialogWindow(Gtk.Window):
    """
    @description: This class show error message dialog
    To show it on nay page just import the class and then
        win = MessageDialogWindow()
        win.show_error_message()
        win.show_all()
    @param: text
        text will show in the dialog
    """

    def __init__(self, text):
        Gtk.Window.__init__(self)
        self.text = text

    def show_error_message(self):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.ERROR,
                                   Gtk.ButtonsType.CANCEL,
                                   "Error")
        dialog.format_secondary_text(self.text)
        dialog.run()
        print("Error dialog closed")

        dialog.destroy()

def get_battery_info():
    # This function will return battery info
    # Calling 'acpi -b' shell command and parsing output.
    command = "acpi -b"
    process = subprocess.Popen(command, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if output:
        output = output.decode("utf-8", "strict")[:-1]
        output = output.replace(',', '')
        output = output.split(' ')
        return output
    else:
        error_dialog = MessageDialogWindow(error)
        error_dialog.show_error_message()
        sys.exit(0)

# Declaring variables, for state 1 = Charging, 2 = Discharging, 3 = Not Charging
current_state = 0
previous_state = 0
path = os.path.dirname(os.path.abspath(__file__))
icon_path = path+'/icons'

# Getting battery info
output = get_battery_info()

# Initializing Notify
if 'Battery' in output:
    Notify.init("Battery Monitor")
    notifier = Notify.Notification.new('Battery Monitor', 'Congrats! Battery '
                                                          'is '
                                                   'present.', icon_path +
                                "/icon.png")
    notifier.set_urgency(Notify.Urgency.CRITICAL)
    notifier.show()
else:
    Notify.init("Battery Monitor")
    notifier = Notify.Notification.new('Battery Monitor', 'Battery is not yet '
                                                   'plugged in!.', icon_path +
                                "/icon.png")
    notifier.set_urgency(Notify.Urgency.CRITICAL)
    notifier.show()
    notifier.close()
    Notify.uninit()
    sys.exit(0)

# Showing notification on parsed output
while 'Battery' in output:
    battery_percentage = output[3]
    if len(output) > 4:
        remaining_time = output[4]

        if 'Charging' in output:
            current_state = 0
            if current_state is not previous_state:
                message = 'Now ' + battery_percentage + ', ' + \
                          remaining_time + ' ' + 'until charged!'
                notifier.update('Charging', message, icon = icon_path +
                                                       '/charging.png')
                notifier.show()
                notifier.close()
        else:
            current_state = 1
            if current_state is not previous_state:
                message = 'Now ' + battery_percentage + ', ' \
                                                                          '' + \
                          remaining_time + ' ' + 'remaining!'
                notifier.update('Discharging', message, icon = icon_path +
                                                          '/discharging.png')
                notifier.show()
                notifier.close()
    else:
        current_state = 2
        if current_state is not previous_state:
            message = battery_percentage + ' remaining!'
            notifier.update('Not Charging', message, icon = icon_path +
                                                          '/not-charging.png')
            notifier.show()
            notifier.close()
    previous_state = current_state
    output = get_battery_info()