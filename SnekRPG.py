#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class SnekRPG(Widget):
	player = ObjectProperty(None)
	pass
	
class SnekRPGApp(App):
	def build(self):
		return SnekRPG()
		
class SnekPlayer(Widget):
	pass
		
if __name__ == "__main__":
	SnekRPGApp().run()