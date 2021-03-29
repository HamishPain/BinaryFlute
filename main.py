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

global harmony_list
harmony_key_map = {'h':0,'y':1,'j':2,'u':3,'k':4,'i':5,'l':6,'o':7,';':8,'p':9,'\'':10,'[':11,']':12,}
harmony_vol_map = [0 for _ in range(13)]
harmony_vol = 0.3
harmony_freq_list = [noteToHz(root_midi_note+change_note+index) for index in range(13)]

key_press_map = {}

# Sets fundamental frequency.
# Sets the highest harmonic.s
high = 20

# Creates all sine waves at once.
# a = Sine(freq=freq, mul=0.5)
wave = SquareTable()
osc = OscLoop(wave, freq=harmony_freq_list, mul=harmony_vol_map)
verb = Freeverb(osc, damp=1).out()

a = wave
a.mul = 0

s.start()

import keyboard

pitch_shift_key_map = {'a':-1, 's':-2,'d':-4,'f':-8,'q':1,'w':2,'e':4,'r':8}
vol_shift_key_map = {'c':0.5}
reset_key_map = {' ':0}


def change_pitch_on_press(event: keyboard._Event):
  global key_press_map
  
  if not event.name in key_press_map:
    key_press_map[event.name] = keyboard.KEY_UP

  if event.event_type == key_press_map[event.name]:
    return

  if event.event_type == keyboard.KEY_DOWN and key_press_map[event.name] != keyboard.KEY_DOWN:
    if event.name in pitch_shift_key_map:
      global root_midi_note, change_note
      change_note += pitch_shift_key_map[event.name]
      print(root_midi_note,change_note)
  
  key_press_map[event.name] = event.event_type
  harmony_freq_list[0] = noteToHz(root_midi_note+change_note+0)
  osc.freq = harmony_freq_list


# def change_vol_on_press(event: keyboard._Event):
#   if event.event_type == keyboard.KEY_DOWN:
#     if event.name in vol_shift_key_map:
#       a.mul = vol_shift_key_map[event.name]
#   else:
#     a.mul = 0

def reset_on_press(event: keyboard._Event):
  global root_midi_note, change_note, harmony_freq_list, key_press_map

  if not event.name in key_press_map:
    key_press_map[event.name] = keyboard.KEY_UP

  if event.event_type == key_press_map[event.name]:
    return

  if event.event_type == keyboard.KEY_DOWN and key_press_map[event.name] != keyboard.KEY_DOWN:
    change_note = 0
    print(root_midi_note,change_note)

  else:
    # Store new root note on release
    root_midi_note = root_midi_note+change_note
    change_note = 0
    print(root_midi_note,change_note)

  key_press_map[event.name] = event.event_type

def change_harmony_on_press(event: keyboard._Event):
  global harmony_key_map, harmony_vol, harmony_vol_map, key_press_map

  if not event.name in key_press_map:
    key_press_map[event.name] = keyboard.KEY_UP

  if event.event_type == key_press_map[event.name]:
    return

  if event.event_type == keyboard.KEY_DOWN and key_press_map[event.name] != keyboard.KEY_DOWN:
    index = harmony_key_map[event.name]
    harmony_vol_map[index] = harmony_vol
    harmony_freq_list[index] = noteToHz(root_midi_note+change_note+index)
    
  else:
    index = harmony_key_map[event.name]
    harmony_vol_map[index] = 0

  osc.mul = harmony_vol_map
  osc.freq = harmony_freq_list
  key_press_map[event.name] = event.event_type
  print("Changed")


# keyboard.on_press(on_pressed)
for key in pitch_shift_key_map.keys():
  keyboard.hook_key(key, change_pitch_on_press, suppress=True)

for key in harmony_key_map.keys():
  keyboard.hook_key(key, change_harmony_on_press, suppress=True)

for key in reset_key_map.keys():
  keyboard.hook_key(key, reset_on_press, suppress=True)

while True:
  pass
