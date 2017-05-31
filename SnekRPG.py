#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty, StringProperty
from kivy.vector import Vector
from kivy.clock import Clock
from kivy.uix.button import Button

from math import sqrt

class SnekRPG(Widget):
	player = ObjectProperty(None)
	mainmenu = ObjectProperty(None)
	
	scene = StringProperty('menu')
	
	def init(self):
		self.player.init(self)
		self.mainmenu.center = self.center
	
	def update(self, dt):
		self.player.tick_move(self)
		
	def on_touch_move(self, touch):
		self.player.update_move_to(self, touch.x, touch.y)
				
	def on_touch_up(self, touch):
		self.player.update_move_to(self, touch.x, touch.y)
		
	def get_bounds(self, obj):
		return Vector(0, 0), Vector(self.width - obj.width, self.height - obj.height)
		
	pass
	
class SnekRPGApp(App):
	def build(self):
		game = SnekRPG()
		game.init()
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game

class MainMenu(Widget):		
	pass
		
class SnekPlayer(Widget):
	speed = NumericProperty(3)
	floatpos = ListProperty()
	destination = ListProperty()
	
	lastmove = ListProperty()
	last = NumericProperty(0)
	
	def init(self, parent):
		self.size = Vector(32, 32)
		self.update_move_to(parent, parent.width / 2, parent.height / 2)
		
	def tick_move(self, parent):
		temp_min, temp_max = parent.get_bounds(self)
		
		destination = Vector(self.destination)
		floatpos = Vector(self.floatpos)
		if destination.x < floatpos.x:
			temp_min.x = destination.x
		else:
			temp_max.x = destination.x
		if destination.y < floatpos.y:
			temp_min.y = destination.y
		else:
			temp_max.y = destination.y
		
		move = Vector(self.destination) - self.pos
		norm = sqrt(move.x * move.x + move.y * move.y)
		if norm > self.speed:
			norm /= self.speed
		if norm <= 1:
			return
		move /= norm
		
		newpos = move + self.floatpos
		
		if newpos.x < temp_min.x:
			newpos.x = temp_min.x			
		if newpos.y < temp_min.y:
			newpos.y = temp_min.y
		if newpos.x > temp_max.x:
			newpos.x = temp_max.x	
		if newpos.y > temp_max.y:
			newpos.y = temp_max.y	
			
		self.floatpos = newpos
		self.x = round(newpos.x)
		self.y = round(newpos.y)
		
	def update_move_to(self, parent, x, y):
		temp_min, temp_max = parent.get_bounds(self)
		if x < temp_min.x:
			x = temp_min.x			
		if y < temp_min.y:
			y = temp_min.y			
		if x > temp_max.x:
			x = temp_max.x
		if y > temp_max.y:
			y = temp_max.y

		self.floatpos = self.pos
		self.destination = (x, y)
#	
	pass
		
if __name__ == "__main__":
	SnekRPGApp().run()