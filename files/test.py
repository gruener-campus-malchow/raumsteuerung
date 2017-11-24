#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sound import Sound
#from pumpe import Pumpe
from buzzer import Buzzer
from dc import DC
from pumpe import Pumpe

soundModul= Sound('testSoundModul')
soundModul.test()

#pumpModul = Pumpe('testPumpe')
#pumpModul.test()

buzzerModul = Buzzer('testBuzzer')
buzzerModul.test()

#dualColorModul = DC('test dual Color')
#dualColorModul.test()

pumpe = Pumpe()
pumpe.test()
