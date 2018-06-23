import csv
from sys import argv
import numpy as np

from utils.datapaths import *
from ml.linear_classifier import LinearClassifier
from utils.gesture import Gesture

def get_classifier(name):
    classifier = LinearClassifier(9, len(Gesture))
    classifier.fromFile(classifier_path(name))
    return classifier

# Takes a CSV of sample EMG data (8 numbers per row) and predicts its
# matching gestures va a specified classifier
def main(emg_path, name):
    classifier = get_classifier(name)

    with open(sample_data_path(emg_path), 'rb') as emg_file:
        reader = csv.reader(emg_file)
        for row in reader:
            assert len(row) == 8
        
            gesture_num = get_gesture(row, classifier)
            gesture_name = Gesture(gesture_num).name
            print(' '.join(row) + ' ' + str(gesture_name))

def get_gesture(emg, classifier):
    emg_features = np.array(list(emg)).astype(float)
    emg_features /= 1000.0
    add_one = np.ones((1,9))
    add_one[0,:-1] = emg_features
    
    emg_features = add_one
    return classifier.predict(emg_features)[0]

if __name__ == '__main__':
    # Arguments are file names of the sample EMG file and the classifier to use for predictions 
    if len(argv) < 2:
        sample = 'sample.csv'
    else: sample = argv[1]

    if len(argv) < 3:
        classifier = classifier_default_name()
    else: classifier = argv[2]

    main(sample, classifier)
