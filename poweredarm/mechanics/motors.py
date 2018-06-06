import pigpio
import time

gpio = pigpio.pi()

##GPIO Num for Each Finger
thumbGPIO = 26
indexGPIO = 19
midGPIO = 13
ringGPIO = 16
pinkyGPIO = 20  #gpio20, pin 38

## Fully Extended and Fully Contracted Values for Each Finger
thumbEx = 12.5
thumbCon = 7
indexEx = 4
indexCon = 8
midEx = 10
midCon = 5.5
ringEx = 4
ringCon = 7.5
pinkyEx = 4
pinkyCon = 8.5

## Importing the Required Libraries 
import RPi.GPIO as IO

## Initialization 
IO.setwarnings(False)
IO.setmode (IO.BCM)
IO.setup(thumbGPIO,IO.OUT)
IO.setup(indexGPIO,IO.OUT)
IO.setup(midGPIO,IO.OUT)
IO.setup(ringGPIO,IO.OUT)
IO.setup(pinkyGPIO,IO.OUT)

## Assign Pins to Each Finger
pThumb = IO.PWM(thumbGPIO,50)
pIndex = IO.PWM(indexGPIO,50)
pMid = IO.PWM(midGPIO,50)
pRing = IO.PWM(ringGPIO,50)
pPinky = IO.PWM(pinkyGPIO,50)

# Interfaces for all 4 of the below functions must exist
def openGrip():
    pThumb.ChangeDutyCycle(thumbEx)
    pIndex.ChangeDutyCycle(indexEx)
    pMid.ChangeDutyCycle(midEx)
    pRing.ChangeDutyCycle(ringEx)
    pPinky.ChangeDutyCycle(pinkyEx)
    
def closedGrip():
    pThumb.ChangeDutyCycle(thumbCon)
    pIndex.ChangeDutyCycle(indexCon)
    pMid.ChangeDutyCycle(midCon)
    pRing.ChangeDutyCycle(ringCon)
    pPinky.ChangeDutyCycle(pinkyCon)

def keyGrip():
    pThumb.ChangeDutyCycle(thumbCon)
    pIndex.ChangeDutyCycle(indexCon)
    pMid.ChangeDutyCycle(midEx)
    pRing.ChangeDutyCycle(ringEx)
    pPinky.ChangeDutyCycle(pinkyEx)

def startHand():
    pThumb.start(thumbEx)
    pIndex.start(indexEx)
    pMid.start(midEx)
    pRing.start(ringEx)
    pPinky.start(pinkyEx)
