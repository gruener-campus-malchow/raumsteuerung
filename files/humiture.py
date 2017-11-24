#!/usr/bin/python3
# author = HansSarpeiDerKing
from sensor import Sensor 
import random

class Humiture(Sensor):

	def __init__(self):
		self._temperature = 0
		self._humiture = 0

	def setTemperature(self, temperature):
		self._temperatur = temperature
		
	def getTemperature(self):
		return temperature
	
	def setHumiture(self, humiture):
		self._humiture = humiture
		
	def getHumiture(self):
		return humiture

	def test(self):
		
		ranStat = random.randrange(0, 1000)
		print('test-start gesetzte temperature mit setTemperature(): '+str(self.setTemperature(randStat())+'°C')
		print('test Ergebnisse getTemperature(): '+str(self.getTemperature()+'°C')
		print('test-start gesetzte humiture mit setHumiture(): '+str(self.setHumiturre(randStat())+'%')
		print('test Ergebnisse getHumiture(): '+str(self.getHumiturre()+'%')

