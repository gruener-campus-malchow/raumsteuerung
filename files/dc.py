#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author = Backerich

import random as rn

from aktor import Aktor

class DC(Aktor):

	def __init__(self, bezeichnung, status=0, red=0, green=0):
		Aktor.__init__(self, bezeichnung, status)
		self._red = red
		self._green = green
	
	def showColor(self):
		print('Red: ' + str(self._red) + ' Green: ' + str(self._green))
	
	def changeColor(self, red, green):
		self._red = red
		self._green = green
	
	def test(self):
		print("Ich bin die Dual Color LED Test Datei.")
		self.showColor()
		print("Ändert Farben...")
		self.changeColor(rn.randrange(1, 10), rn.randrange(1, 10))
		self.showColor()
