#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author = Backerich

from modul import Modul

class Sensor(Modul):

	def __init__(self, bezeichnung, status):
		self._messwert = []
		Modul.__init__(self, bezeichnung, status)

	def addMesswert(self, messwert):
		self._messwert.insert(len(self._messwert),messwert)
