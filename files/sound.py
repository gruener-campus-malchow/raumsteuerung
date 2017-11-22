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
