#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Modul(object):

	def __init__(self, bezeichnung, status):
		self._bezeichnung = bezeichnung
		self._status = status
	
	def getBezeichnung(self):
		print(self._bezeichnung)
	
	def getStatus(self):
		print(self._status)
	
	def setStatus(self):
		self._status ^= 1
