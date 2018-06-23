import math
import pdb
import os
import csv
import numpy as np

from ml.linear_classifier import LinearClassifier
from ml import use_svm
from mechanics import motors
from utils.gesture import Gesture
from utils.datapaths import *

# There will always be as many classes as there are gestures
classifier = LinearClassifier(9, len(Gesture))

# Main emg processing function
def proc_emg(emg, moving, times = []):    
    gesture = use_svm.get_gesture(emg, classifier)
    motors.do_gesture(gesture)

    print(str(emg) + ' ' + str(Gesture(gesture).name))

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

