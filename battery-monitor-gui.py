import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class ListBoxRowWithData(Gtk.ListBoxRow):
    def __init__(self, data):
        super(Gtk.ListBoxRow, self).__init__()
        self.data = data
        self.add(Gtk.Label(data))

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title='Battery Monitor')
        self.set_border_width = 10
        self.box = Gtk.Box(spacing=6)
        self.add(self.box)


win = MainWindow()
win.connect('delete_event', Gtk.main_quit)
win.show_all()
Gtk.main()