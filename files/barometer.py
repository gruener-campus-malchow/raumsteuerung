#!/usr/bin/python3
#creator ZoccaX
from sensor import Sensor

class Barometer(Sensor): 

	def __init__(self):
		
		self._temperature = []
		self._pressureValue = []

	def getTemperature(self):
		return(self._temperature)

	def getPressureValue(self):
		return(self._pressureValue)
