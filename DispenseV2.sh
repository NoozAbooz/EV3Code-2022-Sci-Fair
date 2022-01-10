#!/bin/bash

# Set variables
MASKS="$1"

export MC=/sys/class/tacho-motor/motor0
echo brake > $MC/stop_action

# Dispense code
dispense_mask () {

  echo 1000 > $MC/speed_sp
  echo 100 > $MC/time_sp
  echo run-timed > $MC/command

  sleep 0.080

  echo -1050 > $MC/speed_sp
  echo 750 > $MC/time_sp
  echo run-timed > $MC/command

  sleep 0.800

  echo 1050 > $MC/speed_sp
  echo 250 > $MC/time_sp
  echo run-timed > $MC/command
}

for i in $( eval echo {1..$MASKS}) 
do
  dispense_mask
done

beep
