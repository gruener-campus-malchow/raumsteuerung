#!/usr/bin/env python3

from modul import Modul

class Aktor(Modul):

	def __init__(self, bezeichnung, status):
		Modul.__init__(self, bezeichnung, status)