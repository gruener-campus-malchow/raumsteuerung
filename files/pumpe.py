#!/usr/bin/python3#
# -*- coding: utf-8 -*-
#Author: ZoccaX
from aktor import Aktor
import random
import time

class Pumpe(Aktor):

	def __init__(self):
		self._wassermenge = 0

	def setWassermenge(self, wassermenge):
		self._wassermenge = wassermenge

	def getWassermenge(self):
		return self._wassermenge

	def test(self):
		start = time.time()
		print('The testfunction of Pumpe starts:')

		for i in range(1, 100):
			randStat = random.randrange(100, 1000)
			self.setWassermenge(randStat)
			print('setWassermenge(): '+ str(randStat) + ' L/h, ' ,
					'getWassermenge()' + str(self.getWassermenge()) + ' L/h')

		end = time.time()
		dauer = end -start
		print('The test-function of Pumpe end and took ' + str(dauer) + 'seconds.')

testPumpe = Pumpe()
testPumpe.test()
