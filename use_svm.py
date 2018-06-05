from Linear_Classifier import linear_classifier
from scripts.common.gesture import Gesture
import csv
from sys import argv
import numpy as np

def classifier_path(name):
    return 'Linear_Classifier/linear_classifier_' + name + '.csv'
     
def get_classifier(name):
    classifier = linear_classifier.LinearClassifier(9, len(Gesture))
    classifier.fromFile(classifier_path(name))
    return classifier

# Takes a CSV of sample EMG data (8 numbers per row) and predicts its
# matching gestures va a specified classifier
def main(emg_path, name):
    classifier = get_classifier(name)

    with open('Sample_Prediction_Data/' + emg_path, 'rb') as emg_file:
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
    # Arguments are name of the sample EMG file and the name of the classifier to use
    if len(argv) < 2:
        path = 'sample.csv'
    else: path = argv[1]

    if len(argv) < 3:
        name = "1"
    else: name = argv[2]

    main(path, name)
