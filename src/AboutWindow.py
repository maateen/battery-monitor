#!/usr/bin/env python3

# third-party library
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import GdkPixbuf

# imports from current project
from config import ICONS



class AboutWindow():
    """GUI class for About Window.

    This class displays the About window in where the user can see the information about Battery Monitor project.
    """

    def __init__(self):
        authors = [
            'Maksudur Rahman Maateen <https://maateen.me/>',
            'Safwan Rahman <https://github.com/safwanrahman>',
            'Abdelhak BOUGOUFFA <https://abougouffa.github.io/>'
        ]
        documenters = [
            'Maksudur Rahman Maateen <https://maateen.me/>',
        ]

        # initiaing about dialog and params
        self.about_dialog = Gtk.AboutDialog()
        self.about_dialog.set_program_name('Battery Monitor')
        self.about_dialog.set_version('v0.6')
        self.about_dialog.set_copyright('Copyright \xa9 2016-2018 Maksudur Rahman Maateen')
        self.about_dialog.set_website_label('Official Website')
        self.about_dialog.set_website('http://battery-monitor.maateen.me/')
        self.about_dialog.set_comments('Battery Monitor is a utility tool developed on Python3 and PyGtk3. It will notify the user about charging, discharging, not charging and critically low battery state of the battery on Linux (surely if the battery is present).')
        self.about_dialog.set_license_type (Gtk.License.GPL_3_0,)
        self.about_dialog.set_default_icon_from_file(ICONS['app'])
        self.about_dialog.set_logo(GdkPixbuf.Pixbuf.new_from_file_at_size(ICONS['app'], 64, 64))
        self.about_dialog.set_authors(authors)
        self.about_dialog.set_documenters(documenters)
        self.about_dialog.add_credit_section('AUR maintained by', ['Yochanan Marqos <https://github.com/yochananmarqos>'])
        self.about_dialog.set_title('About Battery Monitor')
        self.about_dialog.connect('response', self.__close)

    def show(self):
        # show the about dialog.

        self.about_dialog.show()

    def __close(self, action, parameter):
        """Called when the user wants to close the about dialog.

        @param: action
            the window to close
        """
        action.destroy()
