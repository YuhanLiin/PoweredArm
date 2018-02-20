# EMG Data Processing Script
print("Emg Data Processing")

import math
import pdb
import os
import datetime
import csv
import numpy as np
import pigpio
from Linear_Classifier import linear_classifier
import time

classifier = linear_classifier.LinearClassifier(9,3)
gpio = pigpio.pi()

start_time = datetime.datetime.now()
training_data = {'file':None, 'csv_writer':None}

# Mode options: 'training', 'predicting'
mode = 'predicting'

# Label options: 'rest', 'grip', 'flex', TODO: 'key'
label = 'flex'

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

# Labels stored in csv as integers: rest -> 0, grip -> 1, flex -> 2 
def label_to_int(gesture_label):
        if (gesture_label == 'rest'):
                return 0
        if (gesture_label == 'grip'):
                return 1
        if (gesture_label == 'flex'):
                return 2
        return -1


# Display emg data in human-readable way
def print_emg(emg):
        secondsSinceStart = (datetime.datetime.now().second-start_time.second+60)%60

	os.system('clear')
        for datum in emg:
                print('[' + '*'*int(datum/100))
        print ("EMG: " + str(emg) + " Seconds: " + str(secondsSinceStart))

# Control motors by gesture
def move_motors(gesture):
        # Rest: turn motor off
        if (gesture == 0):
##                gpio.write(4,0)
##                gpio.write(3,0)
                openGrip()
        # Grip: move motor forward
        if (gesture == 1):
##                gpio.write(4,0)
##                gpio.write(3,1)
                closedGrip()
        # Flex: move motor backward
        if (gesture == 2):
##                gpio.write(4,1)
##                gpio.write(3,0)
                keyGrip()

# Main emg processing function
def proc_emg(emg, moving, times = []):

	#print_emg(list(emg))
##	print("your sexy")
	
        if (mode == 'training' and training_data['csv_writer']):
                # Each row of training data contains 8 EMG samples followed by associated label
                training_data['csv_writer'].writerow(list(emg)+[label_to_int(label)])

        elif(mode == 'predicting' and classifier):
                gesture = -1
                
                add_one = np.ones((1,9))
                emg_features = np.array(list(emg)).astype(float)
                emg_features /= 1000.0
                add_one[0,:-1] = emg_features
                
                emg_features = add_one
##                print(emg_features)
                gesture = classifier.predict(emg_features)                
##                if (gesture == 0):
##                        print('RESTING!')
##                if (gesture == 1):
##                        print('GRIPPING!')
##                if (gesture == 2):
##                        print('FLEXING!')
                move_motors(gesture)


# onPeriodic() is called periodically while the myo is connected.

# Myo will be locked on first call, at which point we must onlock it,
# set up global variables for runtime, and add emg processing handler.

def onPeriodic():

        # If myo is locked, unlock it and initialize script variables
	if not(myo.isUnlocked()):
                if (mode == 'training'):

                        if (training_data['file'] != None):
                                training_data['file'].close()

                        training_data['file'] = open(label+'_'+datetime.datetime.now().strftime("%Y-%m-%d@%H-%M-%S")+'.csv','w+')
                        training_data['csv_writer'] = csv.writer(training_data['file'])

                elif (mode == 'predicting'):
                        
                        ## START THE PINS
                        pThumb.start(thumbEx)
                        pIndex.start(indexEx)
                        pMid.start(midEx)
                        pRing.start(ringEx)
                        pPinky.start(pinkyEx)
                        classifier.fromFile('Linear_Classifier/greg_rest_grip_flex_linear_classifier_1_99p.csv')

                myo.unlock("hold")
                myo.start_raw()
                myo.add_emg_handler(proc_emg)

        # Script is running   
        else:
##                print(myo.conn)
                1



def onUnlock():
	print("onUnlock")
	myo.rotSetCenter()
	myo.unlock("hold")
