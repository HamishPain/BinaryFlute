from pyo import *
import pyo
import math
def noteToHz(num):
  return pow(2,(num-69)/12)*440

s = Server().boot()

### Using multichannel-expansion to create a square wave ###
global root_midi_note
root_midi_note = 76
change_note = 0
freq = noteToHz(76+change_note)

# Sets fundamental frequency.
# Sets the highest harmonic.s
high = 20

# Creates all sine waves at once.
a = Sine(freq=freq, mul=0.5)
a.mul = 0

c = Harmonizer(a, transpo=4)
# Prints the number of streams managed by "a".
print(len(a))

# The mix(voices) method (defined in PyoObject) mixes
# the object streams into `voices` streams.
b = c.mix(voices=1).out()


# Displays the waveform.
# sc = Scope(b)

# s.gui(locals())
s.start()

import keyboard

pitch_shift_key_map = {'a':-1, 's':-2,'d':-4,'f':-8,'q':1,'w':2,'e':4,'r':8}
vol_shift_key_map = {'c':0.5}
reset_key_map = {'v':0}


def change_pitch_on_press(event: keyboard._Event):
  if event.event_type == keyboard.KEY_DOWN:
    if event.name in pitch_shift_key_map:
      global root_midi_note, change_note
      change_note += pitch_shift_key_map[event.name]
      freq = noteToHz(root_midi_note+change_note)
      a.freq = freq
      print(root_midi_note,change_note)

def change_vol_on_press(event: keyboard._Event):
  if event.event_type == keyboard.KEY_DOWN:
    if event.name in vol_shift_key_map:
      a.mul = vol_shift_key_map[event.name]
  else:
    a.mul = 0

def reset_on_press(event: keyboard._Event):
  global root_midi_note, change_note
  if event.event_type == keyboard.KEY_DOWN:
    change_note = 0
    freq = noteToHz(root_midi_note+change_note)
    a.freq = freq
    print(root_midi_note,change_note)
  else:
    # Store new root note on release
    root_midi_note = root_midi_note+change_note
    print(root_midi_note,change_note)

# keyboard.on_press(on_pressed)
for key in pitch_shift_key_map.keys():
  keyboard.hook_key(key, change_pitch_on_press, suppress=True)

for key in vol_shift_key_map.keys():
  keyboard.hook_key(key, change_vol_on_press, suppress=True)

for key in reset_key_map.keys():
  keyboard.hook_key(key, reset_on_press, suppress=True)

while True:
  pass
