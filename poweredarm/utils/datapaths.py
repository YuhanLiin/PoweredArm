# Returns path names to CSV data relative to the project root

def classifier_dirname(): return 'Linear_Classifier/'
def classifier_path(filename): return 'data/' + classifier_dirname() + filename
def classifier_default_name(): return 'linear_classifier_default.csv'

def sample_data_dirname(): return 'Sample_Prediction_Data/'
def sample_data_path(filename): return 'data/' + sample_data_dirname() + filename

def emg_training_dirname(): return 'EMG_Training_Data/'
def emg_training_path(filename): return 'data/' + emg_training_dirname() + filename

