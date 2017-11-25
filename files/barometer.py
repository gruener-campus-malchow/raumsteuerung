#!/usr/bin/python3
# -*- coding: utf-8 -*-
#author: ZoccaX
from sensor import Sensor
import random
import time

class Barometer(Sensor):

	def __init__(self):

		self._temperature = []
		self._pressureValue = []

	def getTemperature(self):
		return self._temperature

	def getPressureValue(self):
		return self._pressureValue

	def test(self):

		start = time.time()
		print('The testfunction of Barometer starts:')

		values = 100 # Anzahl der Testwerte (n>1)
		for _ in range(1, values):
			self._temperature.append(random.randrange(0, 50))
			self._pressureValue.append(random.randrange(0, 1000))

		print('Temperatur mit getTemperature'+ str(self._temperature) + ' L/s')
		print('Luftdruck mit getLuftdruck'+ str(self._pressureValue) + ' L/s')

		end = time.time()
		dauer = end -start
		print('The test-function of Barometer ends and took ' + str(dauer) + 'seconds.')

testBarometer = Barometer()
testBarometer.test()
