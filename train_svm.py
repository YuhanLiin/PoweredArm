import os
import csv
from sys import argv
import numpy as np
from Linear_Classifier.linear_classifier import LinearClassifier

def make_master_data(path):
    csv_files = (os.path.join(path, name) for name in os.listdir(path) if name.lower().endswith('.csv'))
    master_data = []

    for csv_file in csv_files:
        f = open(csv_file, 'r')
        reader = csv.reader(f)
        
        contents = list(reader)
        num_rows = len(contents)

        for row in contents[int(0.1*num_rows):int(0.9*num_rows)]:
            master_data.append(row)

        f.close()

    return master_data

def get_master_data(path):
    data = np.array(make_master_data(path))
    data = data.astype(float)
    
    X = data[:,:-1]
    X /= 1000.0
    add_ones = np.ones((X.shape[0],X.shape[1]+1))
    add_ones[:,:-1] = X
    
    X = add_ones
    y = data[:,-1].astype(int)

    return X, y

def split_data(X, y):
    # Split into train, val, test
    train_idx = np.random.choice(X.shape[0],int(0.8*X.shape[0]),replace=False)
    train_X = X[train_idx]
    train_y = y[train_idx]

    X = np.delete(X,train_idx,axis=0)
    y = np.delete(y,train_idx,axis=0)
    
    val_idx = np.random.choice(X.shape[0],int(0.5*X.shape[0]),replace=False)
    
    val_X = X[val_idx]
    val_y = y[val_idx]

    test_X = np.delete(X,val_idx,axis=0)
    test_y = np.delete(y,val_idx,axis=0)

    print('Shapes for Chad\'s comfort')
    print(train_X.shape, train_y.shape, val_X.shape, val_y.shape, test_X.shape, test_y.shape)

    return train_X, train_y, val_X, val_y, test_X, test_y

# Takes the directory path of the training CSV data and a string to add 
# to the file name of output classifier
def main(path = 'EMG_Training_Data', classifier_name = '1'):
    num_classes = 3
    X, y = get_master_data(path)
    train_X, train_y, val_X, val_y, test_X, test_y = split_data(X, y)

    # hyperparams
    learning_rates = [1]
    reg_strengths = [0]
    num_iters = 5000

    best_model = None
    best_accuracy = -1

    results = {}

    for lr in learning_rates:
        for rs in reg_strengths:
            
            this_model = LinearClassifier(X.shape[1],num_classes)
            this_model.train(train_X, train_y, lr, rs, num_iters)
            y_pred = this_model.predict(val_X)
            val_accuracy = np.mean(y_pred == val_y)
            
            y_pred = this_model.predict(train_X)
            train_accuracy = np.mean(y_pred == train_y)
            print('This val accuracy: ' + str(val_accuracy))
            
            if (val_accuracy > best_accuracy):
                best_model = this_model
                best_accuracy = val_accuracy

            results[(lr, rs)] = train_accuracy, val_accuracy
            this_model.print_model()

    for lr, rs in sorted(results):
        train_accuracy, val_accuracy = results[(lr,rs)]
        print('lr %e reg %e train_accuracy %f val_accuracy %f' % (lr, rs, train_accuracy, val_accuracy))

    print(test_X[0])
    y_pred_test = best_model.predict(test_X)

    test_accuracy = np.mean(y_pred_test == test_y)

    print('This test accuracy: ' + str(test_accuracy))
    best_model.toFile(
            'Linear_Classifier/linear_classifier_' + 
            classifier_name + '_' + str(int(test_accuracy*100)) +
            'p.csv')

if __name__ == '__main__':
    main(argv[1], argv[2])
