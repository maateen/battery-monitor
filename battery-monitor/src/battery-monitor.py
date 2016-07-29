import gi

gi.require_version('Gtk', '3.0')
gi.require_version('Notify', '0.7')
from gi.repository import Gtk
from gi.repository import Notify
import os, sys, subprocess, time


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


def main():
    # This is the main function
    try:
        print("Press 'ctrl+C' to exit.")
        # Declaring variables, for state 1 = Charging, 2 = Discharging, 3 = Not Charging
        current_state = 0
        previous_state = 0
        current_battery_percentage = 0
        previous_battery_percentage = 0
        path = os.path.dirname(os.path.abspath(__file__))
        icon_path = path + '/icons'

        # Getting battery info
        output = get_battery_info()

        # Initializing Notify
        if 'Battery' in output:
            Notify.init("Battery Monitor")
            notifier = Notify.Notification.new('Battery Monitor',
                                               'Congrats! Started '
                                               'to '
                                               'monitor just now.', icon_path +
                                               "/icon.png")
            notifier.set_urgency(Notify.Urgency.CRITICAL)
            notifier.show()
        else:
            Notify.init("Battery Monitor")
            notifier = Notify.Notification.new('Battery Monitor',
                                               'Battery is not yet '
                                               'present!', icon_path +
                                               "/icon.png")
            notifier.set_urgency(Notify.Urgency.CRITICAL)
            notifier.show()
            notifier.close()
            Notify.uninit()
            sys.exit(0)

        # Showing notification on parsed output
        while 'Battery' in output:
            battery_percentage = output[3]
            battery_percentage = battery_percentage.strip(' %')
            if len(output) > 4:
                remaining_time = output[4]

                if 'Charging' in output:
                    current_state = 0
                    if current_state is not previous_state:
                        message = 'Now ' + battery_percentage + '%, ' + \
                                  remaining_time + ' ' + 'until charged!'
                        notifier.update('Charging', message, icon=icon_path +
                                                                  '/charging.png')
                        notifier.show()
                        notifier.close()
                else:
                    current_state = 1
                    current_battery_percentage = int(battery_percentage)
                    if current_battery_percentage <= 10 and \
                                    current_battery_percentage is not \
                                    previous_battery_percentage:
                        message = 'Only ' + battery_percentage + '%, ' \
                                                                 '' + \
                                  remaining_time + ' ' + 'remaining!'
                        notifier.update('Critically Low Battery', message,
                                        icon=icon_path +
                                             '/low-battery.png')
                        os.system('play ' + path + '/sound.wav &')
                        notifier.show()
                        notifier.close()
                        previous_battery_percentage = current_battery_percentage
                    # Temporary solution to issue 4
                    # Will make a GUI for this
                    elif current_battery_percentage == 30 and \
                                    current_battery_percentage is not \
                                    previous_battery_percentage:
                        message = 'Now ' + battery_percentage + '%, ' \
                                                                 '' + \
                                  remaining_time + ' ' + 'remaining!'
                        notifier.update('Low Battery', message,
                                        icon=icon_path +
                                             '/low-battery.png')
                        notifier.show()
                        notifier.close()
                        previous_battery_percentage = current_battery_percentage
                    elif current_state is not previous_state:
                        message = 'Now ' + battery_percentage + '%, ' \
                                                                '' + \
                                  remaining_time + ' ' + 'remaining!'
                        notifier.update('Discharging', message, icon=icon_path +
                                                                     '/discharging.png')
                        notifier.show()
                        notifier.close()
                    else:
                        pass
            else:
                current_state = 2
                if current_state is not previous_state:
                    message = battery_percentage + '% remaining!'
                    notifier.update('Not Charging', message, icon=icon_path +
                                                                  '/not-charging.png')
                    notifier.show()
                    notifier.close()

            # Let's delay the loop to minimize CPU usage
            time.sleep(3)
            previous_state = current_state
            output = get_battery_info()

    except:
        print("\nBattery Monitor has been exited successfully.")
        sys.exit(0)

if __name__ == '__main__':
    main()