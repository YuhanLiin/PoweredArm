#!/usr/bin/python

import RPi.GPIO as IO
import time

IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(19,IO.OUT)
p = IO.PWM(19,50)
foo = 7.5
p.start(foo)

while 1:
##    doo = 5 + foo
##    boo = (foo) - 0.5
    p.ChangeDutyCycle(7.5)
##    print(doo)
    time.sleep(0.5)
    p.ChangeDutyCycle(4)
##    print(boo)
    time.sleep(0.5)

while 1:
    p.ChangeDutyCycle(2)
