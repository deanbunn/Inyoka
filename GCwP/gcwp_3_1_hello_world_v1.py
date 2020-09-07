#!/usr/bin/python3

import sys
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class AppWindow(Gtk.ApplicationWindow):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		label = Gtk.Label.new("Howdy Dean!")
		label.set_selectable(True)
		self.add(label)
		self.set_size_request(600, 300)
		label.set_text("Sophie plays ball")


class Application(Gtk.Application):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, application_id="org.example.myapp", **kwargs)
		self.window = None

	def do_activate(self):
		if not self.window:
			self.window = AppWindow(application=self, title="Howdy Dean!")

		self.window.show_all()
		self.window.present()


if __name__ == "__main__":
	app = Application()
	app.run(sys.argv)


