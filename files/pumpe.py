#!/usr/bin/python3
#Author: ZoccaX
from aktor import Aktor
import random

class Pumpe(Aktor): 

	def __init__(self):
		
		self._wassermenge = 0

	def getWassermenge(self):
		return(wassermenge)

	def setWassermenge(self, wassermenge):
		self._wassermenge = wassermenge
		
	def test(self):

	print ('Test-Start gesetzte Wassermenge mit setWassermenge():'+ self.setWassermenge(random.randint(0,1000)) + ' L/s')
	print ('Test-Ergebnisse getWassermenge():'+ self.getWassermenge() + ' L/s')



