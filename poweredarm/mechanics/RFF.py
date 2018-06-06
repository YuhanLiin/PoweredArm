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
import time

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

## START THE PINS
pThumb.start(thumbEx)
pIndex.start(indexEx)
pMid.start(midEx)
pRing.start(ringEx)
pPinky.start(pinkyEx)

def openGrip():
    pThumb.ChangeDutyCycle(thumbEx)
    pIndex.ChangeDutyCycle(indexEx)
    pMid.ChangeDutyCycle(midEx)
    pRing.ChangeDutyCycle(ringEx)
    pPinky.ChangeDutyCycle(pinkyEx)
    return
    
def closedGrip():
    pThumb.ChangeDutyCycle(thumbCon)
    pIndex.ChangeDutyCycle(indexCon)
    pMid.ChangeDutyCycle(midCon)
    pRing.ChangeDutyCycle(ringCon)
    pPinky.ChangeDutyCycle(pinkyCon)
    return

def keyGrip():
    pThumb.ChangeDutyCycle(thumbCon)
    pIndex.ChangeDutyCycle(indexCon)
    pMid.ChangeDutyCycle(midEx)
    pRing.ChangeDutyCycle(ringEx)
    pPinky.ChangeDutyCycle(pinkyEx)
    return

while 1:
    x = input("no: ")
    if(x == 1):
        openGrip()
    elif(x == 2):
        closedGrip()
    elif(x == 3):
        keyGrip()
