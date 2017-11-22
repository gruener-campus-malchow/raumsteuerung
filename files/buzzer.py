#!/usr/bin/env python3

from aktor import Aktor

class Buzzer(Aktor):

	def __init__(self, bezeichnung, status=0, minLautStaerke=0):
		Aktor.__init__(self, bezeichnung, status)
		self._minLautStaerke = minLautStaerke
	
	def showMinLaut(self):
		print(self._minLautStaerke)
	
	def changeMinLaut(self, minLautStaerke):
		self._minLautStaerke = minLautStaerke