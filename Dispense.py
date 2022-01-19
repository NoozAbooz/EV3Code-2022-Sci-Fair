#!/usr/bin/env micropython

# Import functions
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, SpeedRPS
from ev3dev2.sound import Sound
import time
import sys
from threading import Thread

# Define vars
sound = Sound()

mask_count = sys.argv[1] if len(sys.argv) > 1 else "1"
mask_count = int(mask_count)

# Notify not-wearing mask
ttsopts = '-a 200 -s 190 -v'
str_en = "Please wear a mask!"

def runtts():
    sound.speak(str_en, espeak_opts = ttsopts+'en-us')

t = Thread(target=runtts)
t.start()

# Spin da motor
time.sleep(0.5)
for i in range(mask_count):
    print("Dispensing mask number " + str(i+1))
    m = LargeMotor(OUTPUT_A)
    m.on_for_rotations(SpeedPercent(-100), 1.45)
    #m.on_for_rotations(speed=SpeedRPS(2), seconds=1)
    time.sleep(1)

# Beeps to notify it has been dispensed
sound.beep()
