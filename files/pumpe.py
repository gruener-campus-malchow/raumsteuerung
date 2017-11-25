#!/usr/bin/python3#
# -*- coding: utf-8 -*-
#Author: ZoccaX
from aktor import Aktor
import random

class Pumpe(Aktor):

	def __init__(self):
		self._wassermenge = 0

	def setWassermenge(self, wassermenge):
		self._wassermenge = wassermenge

	def getWassermenge(self):
		return self._wassermenge

	def test(self):

		print('testfunction of Pumpe start:')

		for i in range(1, 100):

			randStat = random.randrange(100, 1000)
#			print('Test-Start gesetzte Wassermenge mit setWassermenge():'+ str(randStat) + ' L/h')
#			self.setWassermenge(randStat)
#			print('Test-Ergebnisse getWassermenge():'+ str(self.getWassermenge()) + ' L/h')

			self.setWassermenge(randStat)
			print('setWassermenge(): '+ str(randStat) + ' L/h, ' ,
					'getWassermenge()' + str(self.getWassermenge()) + ' L/h')

		print('test-function of Pumpe end')

testPumpe = Pumpe()
testPumpe.test()
