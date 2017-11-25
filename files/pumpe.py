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

		for i in range(1, 100):

			randStat = random.randrange(0, 1000)
#			print('Test-Start gesetzte Wassermenge mit setWassermenge():'+ str(randStat) + ' L/s')
#			self.setWassermenge(randStat)
#			print('Test-Ergebnisse getWassermenge():'+ str(self.getWassermenge()) + ' L/s')

			print('testPumpe start:')
			self.setWassermenge(randStat)
			print('Gesetzte Wassermenge durch setWassermenge(): '+ str(randStat) + ' L/s' ,
					'Ergebnis aus getWassermenge()' + str(self.getWassermenge()) + ' L/s')

testPumpe = Pumpe()
testPumpe.test()
