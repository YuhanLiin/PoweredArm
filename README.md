# Beowulf-EMG-Classification
Gesture Classification Algorithms

### Current state of this repo:

PyoManager library is used to collect EMG data from the Myo, which is connected to the Raspberry Pi via bluetooth.

There are currently two convenience scripts available. The **train\_svm** script aggregates all csv files produced by the training phase of the Myo script into a linear classifier file. The **use\_svm** scripts applies a linear classifier onto a file of sample EMG data and prints out the gesture predicted for each row. Both scripts must be invoked from the root project directory as such:

`python -m poweredarm.ml.train_svm.py [training_data_dir] [linear_classifier_name]` 
    * **training\_data\_dir:** The directory to search for the csv training data, relative to project root. Default is data/EMG\_Training\_Data.
    * **linear\_classifier\_name:** The name appended to the filename of the linear classifier file generated by the script. Default is '1'.

`python -m poweredarm.ml.use_svm.py [sample_filename] [linear_classifier_name]`
    * **sample\_filename:** The name of the csv file containing the sample EMG data for the prediction. Must be inside data/Sample\_Prediction\_Data. Default is sample.csv.
    * **linear\_classifier\_name:** The name of the classifier used for this prediction. Default is '1'.

Note that if only one argument is provided, then it will go to the first argument while the second argument uses the default.
***
### Gesture recognition is split into three tasks: data collection, training, and prediction.

In the __data collection__ stage, the script is modified so that it simply reads the EMG data and writes it to a file. Before collecting the data, the tester and the user must agree on a gesture to perform. The tester then sets the variable `gesture` in the PyoManager training script to said gesture, the user performs said gesture, and the tester runs the program to collect samples.
The samples will be written to timestamped CSV files, with the first 8 columns representing the emg data as floats and the final column will be an integer representing the gesture being performed.

In the __training__ stage, the data is amalgamated into one master collection and fed into the `train()` method of a Classifier. train_svm.py does this on an example linear classifier.
Once the classifier has been trained and tested using proper practices, it can be used for gesture prediction. To do this, simply call the `toFile()` method of the classifier once it has been trained and tests with sufficient accuracy (train_svm.py handles this).

In the __prediction__ stage, a classifier is loaded from file using the `fromFile()` method. It can then be inserted into the PyoManager predicting script, which accepts new emg data from the Myo and can return its prediction as to the associated gesture.
