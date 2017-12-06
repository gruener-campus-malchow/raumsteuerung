#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author = HansSarpeiDerKing
from sensor import Sensor
import random
import time

class Humiture(Sensor):

        def __init__(self):

                self._temperature = []
                self._humiture = []

        def getTemperature(self):
                return self._temperature

        def getHumiture(self):
                return self._humiture

        def test(self):

                start = time.time()
                print('The testfunction of Humiture starts:')

                values = 100 # Anzahl der Testwerte (n>1)
                for _ in range(1, values):
                        self._temperature.append(random.randrange(0, 50))
                        self._humiture.append(random.randrange(0, 100))

                print('Temperatur mit getTemperature'+ str(self._temperature) + ' C°')
                print('Luftfeuchtigkeit mit getLuftfeuchtigkeit'+ str(self._humiture) + ' %')

                end = time.time()
                dauer = end -start
                print('The test-function of Humiture ends and took ' + str(dauer) + 'seconds.')

testHumiture = Humiture()
testHumiture.test()
