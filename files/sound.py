#!/usr/bin/env python3

from sensor import Sensor

class Sound(Sensor):

	def __init__(self, bezeichnung, status=0):
		Sensor.__init__(self, bezeichnung, status)
	
	def getResult(self):
		print(self._messwert)
	
	def getLastResult(self):
		print(self._messwert[-1])