##GPIO Num for Each Finger
##thumbGPIO = 26
indexGPIO = 19
##midGPIO = 13
##ringGPIO = 16
##pinkyGPIO = 20  #gpio20, pin 38

## Fully Extended and Fully Contracted Values for Each Finger
##thumbEx = 12.5
##thumbCon = 7
indexEx = 4
indexCon = 8
##midEx = 10
##midCon = 5.5
##ringEx = 4
##ringCon = 7.5
##pinkyEx = 4
##pinkyCon = 8.5

## Importing the Required Libraries 
import RPi.GPIO as IO
import time

## Initialization 
IO.setwarnings(False)
IO.setmode (IO.BCM)
##IO.setup(thumbGPIO,IO.OUT)
IO.setup(indexGPIO,IO.OUT)
##IO.setup(midGPIO,IO.OUT)
##IO.setup(ringGPIO,IO.OUT)
##IO.setup(pinkyGPIO,IO.OUT)

## Assign Pins to Each Finger
##pThumb = IO.PWM(thumbGPIO,50)
pIndex = IO.PWM(indexGPIO,50)
##pMid = IO.PWM(midGPIO,50)
##pRing = IO.PWM(ringGPIO,50)
##pPinky = IO.PWM(pinkyGPIO,50)
pIndex.start(4)

##def openGrip(pThumb1,pIndex1,pMid1,pRing1,pPinky1,thumbEx1,indexEx1,midEx1,ringEx1,pinkyEx1):
##    pThumb1.ChangeDutyCycle(thumbEx1)
##    pIndex1.ChangeDutyCycle(indexEx1)
##    pMid1.ChangeDutyCycle(midEx1)
##    pRing1.ChangeDutyCycle(ringEx1)
##    pPinky1.ChangeDutyCycle(pinkyEx1)
##    return
##    
##def closedGrip(pThumb1,pIndex1,pMid1,pRing1,pPinky1,thumbCon1,indexCon1,midCon1,ringCon1,pinkyCon1):
##    pThumb1.ChangeDutyCycle(thumbCon1)
##    pIndex1.ChangeDutyCycle(indexCon1)
##    pMid1.ChangeDutyCycle(midCon1)
##    pRing1.ChangeDutyCycle(ringCon1)
##    pPinky1.ChangeDutyCycle(pinkyCon1)
##    return
##
##def keyGrip(pThumb1,pIndex1,pMid1,pRing1,pPinky1,thumbCon1,indexCon1,midEx1,ringEx1,pinkyEx1):
##    pThumb1.ChangeDutyCycle(thumbCon1)
##    pIndex1.ChangeDutyCycle(indexCon1)
##    pMid1.ChangeDutyCycle(midEx1)
##    pRing1.ChangeDutyCycle(ringEx1)
##    pPinky1.ChangeDutyCycle(pinkyEx1)
##    return

while 1:
    print("run")
##    pThumb.ChangeDutyCycle(thumbEx)
    pIndex.ChangeDutyCycle(8)
##    pMid.ChangeDutyCycle(midEx)
##    pRing.ChangeDutyCycle(ringEx)
##    pPinky.ChangeDutyCycle(pinkyEx)
##    openGrip(pThumb,pIndex,pMid,pRing,pPinky,thumbEx,indexEx,midEx,ringEx,pinkyEx)
##    time.sleep(2)
##    closedGrip(pThumb,pIndex,pMid,pRing,pPinky,thumbCon,indexCon,midCon,ringCon,pinkyCon)
##    time.sleep(2)
##    keyGrip(pThumb,pIndex,pMid,pRing,pPinky,thumbCon,indexCon,midEx,ringEx,pinkyEx)
    time.sleep(2)
    pIndex.ChangeDutyCycle(4)
    time.sleep(2)
    
