
import numpy as np
import csv

class LinearClassifier:
    def __init__(self, num_dim, num_classes):
        std = 0.001

        # Compute Weight matrix with random values (dim x classes)
        self.W = std * np.random.randn(num_dim*num_classes)
        self.W = self.W.reshape((num_dim,num_classes))
        
    def softmax_loss(self, X, y, reg_str):
        loss = 0.0
        dW = np.zeros_like(self.W)
        num_classes = self.W.shape[1]
        num_train = X.shape[0]

        # X is (sample_size x dim), so scores is (sample_Size x classes)
        scores = np.dot(X, self.W)
        scores -= np.max(scores, axis=1, keepdims=True)

        probs = np.exp(scores)/np.sum(np.exp(scores), axis=1, keepdims=True)

        data_loss = -np.sum( np.log(probs[range(num_train),y]) )
        data_loss /= num_train

        loss = data_loss + 0.5 * reg_str * np.sum(self.W * self.W)

        dscores = probs
        dscores[range(num_train), y] -= 1
        dscores /= num_train

        dW = (X.T).dot(dscores)
        dW += reg_str * self.W
        
        return loss, dW

    def train(self, X, y, lr, reg_str, num_iters):

        num_train = X.shape[0]
        batch_size = 35
        
        for iteration in range(num_iters):
            batch_idx = np.random.choice(num_train, batch_size)
            X_batch = X[batch_idx]
            y_batch = y[batch_idx]
            
            loss, dW = self.softmax_loss(X_batch, y_batch, reg_str)
            self.W = self.W - lr * dW

            if (iteration % 500 == 0):
                print('Loss at iteration %d/%d: %f' % (iteration, num_iters, loss))
            
    def predict(self, X):
        scores = np.dot(X, self.W)
        y_pred = np.argmax(scores, axis=1)
        return y_pred

    def print_model(self):
        print('W:')
        print(self.W)

    def toFile(self, filename):
        f = open(filename, 'w')
        writer = csv.writer(f)
        for row in self.W:
            writer.writerow(row)
        f.close()

    def fromFile(self, filename):
        f = open(filename, 'r')
        reader = csv.reader(f)
        self.W = np.array(list(reader)).astype(float)
        f.close()
