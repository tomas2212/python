

# Gtk3
from gi.repository import Gtk
gtkb = Gtk.Builder()
gtkb.add_from_file("client.xml")
gtkb.get_object("main_window").show()
Gtk.main()
