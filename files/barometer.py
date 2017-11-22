#!/usr/bin/python3
#author: ZoccaX
from sensor import Sensor
from random import Randint

class Barometer(Sensor): 

	def __init__(self):
		
		self._temperature = []
		self._pressureValue = []

	def getTemperature(self):
		return(self._temperature)

	def getPressureValue(self):
		return(self._pressureValue)
	
	def test(self):
		print 'Test-Ergebnisse getTemperature():'+ self.getTemperature(random.randint(0,50))
		print 'Test-Ergebnisse getPressureValue():'+ self.getPressureValue(random.randint(0,2000))
