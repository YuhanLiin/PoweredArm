import math
import pdb
import os
import datetime
import csv
import numpy as np

start_time = datetime.datetime.now()
training_data = {'file':None, 'csv_writer':None}

# Label options: 'rest', 'grip', 'flex', TODO: 'key'
label = 'flex'

# Labels stored in csv as integers: rest -> 0, grip -> 1, flex -> 2 
def label_to_int(gesture_label):
    if (gesture_label == 'rest'):
            return 0
    if (gesture_label == 'grip'):
            return 1
    if (gesture_label == 'flex'):
            return 2
    raise ValueError("Invalid gesture %s" % gesture_label)


# Display emg data in human-readable way (Unused for now)
def print_emg(emg):
    secondsSinceStart = (datetime.datetime.now().second-start_time.second+60)%60

    os.system('clear')
    for datum in emg:
            print('[' + '*'*int(datum/100))
    print ("EMG: " + str(emg) + " Seconds: " + str(secondsSinceStart))

# Main emg processing function
def proc_emg(emg, moving, times = []):
    print_emg(emg)
    training_data['csv_writer'].writerow(list(emg)+[label_to_int(label)])


# onPeriodic() is called periodically while the myo is connected.

# Myo will be locked on first call, at which point we must onlock it,
# set up global variables for runtime, and add emg processing handler.

def onPeriodic():

    # If myo is locked, unlock it and initialize script variables
    if not(myo.isUnlocked()):
        if (training_data['file'] != None):
                training_data['file'].close()

        training_data['file'] = open("EMG_Training_Data/"+label+'_'+datetime.datetime.now().strftime("%Y-%m-%d@%H-%M-%S")+'.csv','w+')
        training_data['csv_writer'] = csv.writer(training_data['file'])

        myo.unlock("hold")
        myo.start_raw()
        myo.add_emg_handler(proc_emg)



def onUnlock():
	print("onUnlock")
	myo.rotSetCenter()
	myo.unlock("hold")
