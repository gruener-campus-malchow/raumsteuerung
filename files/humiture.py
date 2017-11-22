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
		
			print ('test-start gesetzte temperature mit setTemperature(): '+self.setTemperature(random.randint(0,50))+'°C')
			print ('test Ergebnisse getTemperature(): '+self.setTemperature()+'°C')
			print ('test-start gesetzte humiture mit setHumiture(): '+self.setHumiturre(random.randint(0,100))+'%')
			print ('test Ergebnisse getHumiture(): '+self.getHumiturre()+'%')
		
	

		
