#!/usr/bin/python3
#Author: ZoccaX
from aktor import Aktor
import random

class Pumpe(Aktor): 

	def __init__(self):
		
		self.wassermenge = 0

	def setWassermenge(self, wassermenge):
		self.wassermenge = wassermenge
	

	def getWassermenge(self):
		return self.wassermenge

		
	def test(self):

		randStat = random.randrange(0, 1000)
 		
		print('Test-Start gesetzte Wassermenge mit setWassermenge():'+ str(randStat) + ' L/s')
		self.setWassermenge(randStat)
		print('Test-Ergebnisse getWassermenge():'+ str(self.getWassermenge()) + ' L/s')

testPumpe = Pumpe()
testPumpe.test()

