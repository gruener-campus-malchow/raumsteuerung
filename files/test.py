#!/usr/bin/env python3

from sound import Sound
#from pumpe import Pumpe
from buzzer import Buzzer
add utf-8 capability to all classes

soundModul= Sound('testSoundModul')
soundModul.test()

#pumpModul = Pumpe('testPumpe')
#pumpModul.test()

buzzerModul = Buzzer('testBuzzer')
buzzerModul.test()
