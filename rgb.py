#!/usr/bin/env python3

from dc import DC

class RGB(DC):

	def __init__(self, bezeichnung, status=0, red=0, green=0, blue=0):
		DC.__init__(self, bezeichnung, status, red, green)
		self._blue = blue
	
	def showColor(self):
		print('Red: ' + str(self._red) + ' Green: ' + str(self._green) + ' Blue: ' + str(self._blue))
	
	def changeColor(self, red, green, blue):
		self._red = red
		self._green = green
		self._blue = blue