#!/usr/bin/env python

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import NumericProperty, ListProperty, ObjectProperty
from kivy.vector import Vector
from kivy.clock import Clock

from math import sqrt

class SnekRPG(Widget):
	player = ObjectProperty(None)
	
	def init(self):
		self.player.init(self)
	
	def update(self, dt):
		self.player.tick_move(self)
		
	def on_touch_move(self, touch):
		self.player.update_move_to(self, touch.x, touch.y)
				
	def on_touch_up(self, touch):
		self.player.update_move_to(self, touch.x, touch.y)
		
	pass
	
class SnekRPGApp(App):
	def build(self):
		game = SnekRPG()
		game.init()
		Clock.schedule_interval(game.update, 1.0/60.0)
		return game
		
class SnekPlayer(Widget):
#	vel_x = NumericProperty(0)
#	vel_y = NumericProperty(0)
	floatpos = ListProperty()
	speed = NumericProperty(3)
	moveto = ListProperty()
	lastmove = ListProperty()
	last = NumericProperty(0)
#		
	def init(self, parent):
		self.update_move_to(parent, parent.width / 2, parent.height / 2)
		
	def tick_move(self, parent):		
		temp_min = Vector(self.width / 2, self.height / 2)
		temp_max = Vector(parent.right - (self.width / 2), parent.height - (self.height / 2))
		move = Vector(self.moveto) - self.pos
		norm = sqrt(move.x * move.x + move.y * move.y)
		if norm > self.speed:
			norm /= self.speed
		if norm <= 1:
			return
		move /= norm
		self.last = sqrt(move.x * move.x + move.y * move.y)
		self.lastmove = move
		
#		move = move + self.pos
#		if move.x < temp_min.x:
#			move.x = temp_min.x			
#		if move.y < temp_min.y:
#			move.y = temp_min.y
#		if move.x > temp_max.x:
#			move.x = temp_max.x	
#		if move.y > temp_max.y:
#			move.y = temp_max.y	
			
		self.floatpos = move + self.floatpos
		self.pos = self.floatpos
		
	def update_move_to(self, parent, x, y):
		temp_min = Vector(0, 0)
		temp_max = Vector(parent.right - self.width, parent.top - self.height)
		if x < temp_min.x:
			x = temp_min.x			
		if y < temp_min.y:
			y = temp_min.y			
		if x > temp_max.x:
			x = temp_max.x			
		if y > temp_max.y:
			y = temp_max.y

		self.floatpos = self.pos
		self.moveto = (x, y)
#	
	pass
		
if __name__ == "__main__":
	SnekRPGApp().run()