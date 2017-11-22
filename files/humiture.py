#!/usr/bin/python3
# author = HansSarpeiDerKing
from sensor import Sensor 
from random import Randint

class Humiture(Sensor)

	def __init__(self):
		self._temperature = []
		self._humiture = []

	def getTemperature(self):
		return self._temperatur
	

	def getHumiture(self):
		return self._humiture

	def test(self):
			print ('test Ergebnisse getTemperature(): '+self.getTemperature(random.randint(0,50))+'°C')
			print ('test Ergebnisse getHumiture(): '+self.getHumiturre(random.randint(0,100))+'%')
		
	

		
