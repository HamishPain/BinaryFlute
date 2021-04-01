# Binary Flute

A python synth that uses my binary flute fingerings. Left hand increments by a binary quantity:

  a  s  d  f |  q  w  e  r

(-1 -2 -4 -8 | +1 +2 +4 +8)

This is added to the root note per press in relative mode and summed together with the root note in absolute mode. Hold Space bar to change to absolute mode, and hold 'n' to play the note.

The right hand can play chords, and these stay relative to the root+changes when they were originally pressed. This allows chords to be semi-independent of the melody.

 h y j u k i l o ; p '  [  ]
 
(0 1 2 3 4 5 6 7 8 9 10 11 12)


# Requirements
Uses the pyo library for sound synthesis and the keyboard library for keyboard inputs, install using
```
pip install -U pyo
pip install -U keyboard

```
## todo
- [x] Implement absolute mode, where each note increment counts against a global thing