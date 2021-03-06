import atexit
import math
import pdb
import os
import datetime
import csv
import numpy as np

from utils.gesture import Gesture
from utils.datapaths import *

start_time = datetime.datetime.now()
training_data = {'file':None, 'csv_writer':None}

gesture = Gesture.Rest

# Display emg data in human-readable way 
def print_emg(emg):
    secondsSinceStart = (datetime.datetime.now().second-start_time.second+60)%60

    os.system('clear')
    for datum in emg:
            print('[' + '*'*int(datum/100))
    print ("EMG: " + str(emg) + " Seconds: " + str(secondsSinceStart))

# Main emg processing function
def proc_emg(emg, moving, times = []):
    print_emg(emg)
    training_data['csv_writer'].writerow(list(emg)+[gesture.value])


# onPeriodic() is called periodically while the myo is connected.

# Myo will be locked on first call, at which point we must onlock it,
# set up global variables for runtime, and add emg processing handler.

def onPeriodic():

    # If myo is locked, unlock it and initialize script variables
    if not(myo.isUnlocked()):
        cleanup()

        filename = gesture.name + '_' + datetime.datetime.now().strftime("%Y-%m-%d@%H-%M-%S") + '.csv'
        training_data['file'] = open(emg_training_path(filename), 'w')
        training_data['csv_writer'] = csv.writer(training_data['file'])

        atexit.register(cleanup)
        myo.unlock("hold")
        myo.start_raw()
        myo.add_emg_handler(proc_emg)

# CSV file will always be closed when PyoConnect exits
def cleanup():
    print("clean")
    if (training_data['file'] != None):
        training_data['file'].close()

