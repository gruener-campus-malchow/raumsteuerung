#!/usr/bin/env python3
#author = gschwarz
from sensor import Sensor
from random import randint

class Sound(Sensor):

	def __init__(self, bezeichnung, status=0):
		Sensor.__init__(self, bezeichnung, status)
	
	def getResult(self):
		return self._messwert
	
	def getLastResult(self):
		return self._messwert[-1]

	def test(self):
		for i in range(0,10):
			self.randomMesswert = randint(0, 20)
			self.addMesswert(self.randomMesswert)
		print('Current results: '+str(self.getResult()))
		print('Last results: '+str(self.getLastResult()))

# here ends the class

newWorldSound = Sound('NWS',1)
newWorldSound.test()
