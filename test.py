from pyo import *
import pyo
import time
s = Server().boot().start()


# sine = Sine().out()
wave = SquareTable()
# osc = Looper(wave, pitch=[100, 200, 300], mul=[0.3,0.3**2,0.3**3],interp=2).out()
osc = Looper(wave, pitch=[100], mul=[0.3],interp=3)
rev = Freeverb(osc.mix(2), size=0.80, damp=0.70, bal=0.30).out()
# harm = Harmonizer(osc, transpo=[12,24,36], mul=[0.3,0.3**2,0.3**3]).out()
# verb = Freeverb(osc).out()
# Freeverb(osc).out()

time.sleep(3)

3,7,10
8,0,3
0,3,7
10,2,5
