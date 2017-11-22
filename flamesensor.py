#!/usr/bin/env python3

from sensor import Sensor

class Flamme(Sensor):

	def __init__(self, bezeichnung, status=0):
		Sensor.__init__(self, bezeichnung, status)
	
	def setAlarm(self):
		if self._messwert[-1] > 60:
			print('ALARM')
			self.sendMessage()

	def sendMessage(self):
		print('MESSAGE')