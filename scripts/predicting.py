import math
import pdb
import os
import csv
import numpy as np
from Linear_Classifier import linear_classifier
from mechanics import motors

classifier = linear_classifier.LinearClassifier(9,3)

# Control motors by gesture
def do_gesture(gesture):
    # Rest: turn motor off
    if (gesture == 0):
            motors.openGrip()
    # Grip: move motor forward
    if (gesture == 1):
            motors.closedGrip()
    # Flex: move motor backward
    if (gesture == 2):
            motors.keyGrip()

# Main emg processing function
def proc_emg(emg, moving, times = []):    
    add_one = np.ones((1,9))
    emg_features = np.array(list(emg)).astype(float)
    emg_features /= 1000.0
    add_one[0,:-1] = emg_features
    
    emg_features = add_one
    gesture = classifier.predict(emg_features)[0]
    print (gesture)
    do_gesture(gesture)


# onPeriodic() is called periodically while the myo is connected.

# Myo will be locked on first call, at which point we must onlock it,
# set up global variables for runtime, and add emg processing handler.

def onPeriodic():

    # If myo is locked, unlock it and initialize script variables
    if not(myo.isUnlocked()):                
        ## START THE PINS
        motors.startHand()
        classifier.fromFile('Linear_Classifier/linear_classifier_1_99p.csv')

        myo.unlock("hold")
        myo.start_raw()
        myo.add_emg_handler(proc_emg)



def onUnlock():
    print("onUnlock")
    myo.rotSetCenter()
    myo.unlock("hold")
