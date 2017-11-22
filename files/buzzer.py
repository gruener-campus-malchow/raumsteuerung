#!/usr/bin/env python3
# author = Backerich

import random as rn

from aktor import Aktor

class Buzzer(Aktor):

	def __init__(self, bezeichnung, status=0, minLautStaerke=0):
		Aktor.__init__(self, bezeichnung, status)
		self._minLautStaerke = minLautStaerke
	
	def showMinLaut(self):
		print("Mindest Lautstärke: " + str(self._minLautStaerke))
	
	def changeMinLaut(self, minLautStaerke):
		self._minLautStaerke = minLautStaerke
	
	def test(self):
		self.showMinLaut()
		self.changeMinLaut(rn.randrange(1, 10))
		self.showMinLaut()
