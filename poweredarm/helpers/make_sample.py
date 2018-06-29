import csv
import os
from sys import argv
from utils.datapaths import *

def training_to_sample_convert(training_path, sample_path):
    with open(training_path, "r") as tf:
        training_data = csv.reader(tf)
        with open(sample_path, "w") as sf:
            sample_csv = csv.writer(sf)
            for row in training_data:
                assert(len(row) >= 8)
                # Assume first 8 values of every row represent the actual EMG data
                emg = row[:8]
                sample_csv.writerow(emg)

def main(training_path, sample_name):
    training_to_sample_convert(training_path, sample_data_path(sample_name))    

if __name__ == '__main__':
    training_path = argv[1]
    
    if len(argv) < 3:
        sample_name = 'sample.csv'
    else:
        sample_name = argv[2]

    main(training_path, sample_name)

