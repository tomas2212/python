# Gtk2 pygtk version
import pygtk
pygtk.require('2.0')
import gtk

# Gtk3 version
# from gi.repository import gtk

class HelloWorld:
  def destroy(self, widget, data=None):
    gtk.main_quit()

  def __init__(self):
    self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
    self.window.connect("destroy", self.destroy)

    self.label = gtk.Label("Hello World")
    self.label.show()
    self.window.add(self.label)
    self.window.show()
    gtk.main()

if __name__ == "__main__":
  HelloWorld()
