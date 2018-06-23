import math
import pdb
import os
import csv
import numpy as np

from ml.linear_classifier import LinearClassifier
from mechanics import motors
from utils.gesture import Gesture
from utils.datapaths import *

classifier = LinearClassifier(9, len(Gesture))

# Main emg processing function
def proc_emg(emg, moving, times = []):    
    # Put a 1 onto the end of the EMG array
    emg_features = np.array(list(emg)).astype(float)
    emg_features /= 1000.0
    add_one = np.ones((1,9))
    add_one[0,:-1] = emg_features
    
    emg_features = add_one
    gesture = classifier.predict(emg_features)[0]
    print (gesture)
    motors.do_gesture(gesture)


# onPeriodic() is called periodically while the myo is connected.

# Myo will be locked on first call, at which point we must onlock it,
# set up global variables for runtime, and add emg processing handler.

def onPeriodic():

    # If myo is locked, unlock it and initialize script variables
    if not(myo.isUnlocked()):                
        ## START THE PINS
        motors.start_hand()
        classifier.fromFile(classifier_path(classifier_default_name()))

        myo.unlock("hold")
        myo.start_raw()
        myo.add_emg_handler(proc_emg)

