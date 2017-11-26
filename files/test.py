#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sound import Sound
from buzzer import Buzzer
from dc import DC
from pumpe import Pumpe
from barometer import Barometer

soundModul= Sound('testSoundModul')
soundModul.test()

buzzerModul = Buzzer('testBuzzer')
buzzerModul.test()

#dualColorModul = DC('test dual Color')
#dualColorModul.test()

pumpe = Pumpe()
pumpe.test()

barometer = Barometer()
barometer.test()
