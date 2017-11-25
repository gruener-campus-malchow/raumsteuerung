#!/usr/bin/python3
# -*- coding: utf-8 -*-
#author: ZoccaX
from sensor import Sensor
import random

class Barometer(Sensor):

	def __init__(self):

		self._temperature = []
		self._pressureValue = []

	def getTemperature(self):
		return self._temperature

	def getPressureValue(self):
		return self._pressureValue

	def test(self):

		for _ in range(1, 100):
			self._temperature.append(random.randrange(0, 50))
			self._pressureValue.append(random.randrange(0, 1000))

		print('Test-Start momnentanige Temperatur mit getTemperature'+ str(self._temperature) + ' L/s')
		print('Test-Start momnentanigeR Luftdruck mit getLuftdruck'+ str(self._pressureValue) + ' L/s')


testBarometer = Barometer()
testBarometer.test()
