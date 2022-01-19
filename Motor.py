#!/usr/bin/env python3

# Import functions
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sound import Sound
import time
#from threading import Thread

# Define vars
sound = Sound()

# Notify not-wearing mask
ttsopts = '-a 200 -s 190 -v'
str_en = "You are not wearing a mask! Please wait for one to be dispensed..."

sound.speak(str_en, espeak_opts = ttsopts+'en-us')

# Spin motor function
def motorA():
    m = LargeMotor(OUTPUT_A)
    m.on_for_rotations(SpeedPercent(-100), 1.48)

#def motorB():
#    m = LargeMotor(OUTPUT_B)
#    m.on_for_rotations(SpeedPercent(-10), 0.8)

# Spin da motor
#motorA()

# Beeps to notify it has been dispensed
time.sleep(1)
sound.beep()