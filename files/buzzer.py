#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author = Backerich

import random as rn
import wave

from aktor import Aktor

class Buzzer(Aktor):

	def __init__(self, bezeichnung, frequenz=[], status=0, minLautStaerke=0):
		Aktor.__init__(self, bezeichnung, status)
		self._minLautStaerke = minLautStaerke
		self._frequez = frequenz
	
	def showMinLaut(self):
		print("Mindest Lautstärke: " + str(self._minLautStaerke))
	
	def changeMinLaut(self, minLautStaerke):
		self._minLautStaerke = minLautStaerke
	
	def outputSound(self):
		with wave.open("Accipiter_castanilius_Lue0060_01.wav", mode="rb") as w:
			print(w.getparams())
	
	def test(self):
		print("Ich bin die Buzzer Test Datei.")

		array = []
		for _ in range(1, 100):
			array.append(rn.randrange(1, 10))

		self.showMinLaut()

		for i in array:
			print("Misst Daten...")
			self.changeMinLaut(i)
			self.showMinLaut()

b = Buzzer("testBuzzer")
b.outputSound()
