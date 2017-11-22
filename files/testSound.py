#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sound import Sound
from random import randint

class Test(object):
	def __init__(self):
		self.newWorldSound = Sound('NWS',1)

	def addRando(self, maximum=5):
		for i in range(0,maximum):
			self.randomMesswert = randint(0, 20)
			self.newWorldSound.addMesswert(self.randomMesswert)

	def showAll(self):
		print('Current results: '+str(self.newWorldSound.getResult()))
		print('Lastäöü results: '+str(self.newWorldSound.getLastResult()))

newTest = Test()
newTest.addRando(10)
newTest.showAll()
