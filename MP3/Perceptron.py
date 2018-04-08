from random import seed, randrange
from copy import deepcopy
import numpy as np

class Preceptron:
    def __init__(self, trainfile_name, testfile_name):
        self.training_classes = []
        self.training_labels = []
        self.testing_classes =  []
        self.testing_labels = []
        self.weight_list = np.zeros((10, 1025))
        self.confusion_matrix = [[0 for i in range(10)] for i in range(10)]

        self.parse_files(trainfile_name, testfile_name)

    def parse_files(self, trainfile_name, testfile_name):
        trainfile = open(trainfile_name, 'r')
        for line in trainfile:
            if len(line) < 32:
                for ch in line:
                    if ch.isdigit():
                        self.training_labels.append(int(ch))
        trainfile.seek(0)
        for label in self.training_labels:
            image = []
            for i in range(32):
                image_line = trainfile.readline()
                for j in range(32):
                    image.append(int(image_line[j]))
            image_line = trainfile.readline()
            for ch in image_line:
                if ch.isdigit() and int(ch) != label:
                    print('TRAINFILE ALIGN ERROR')
            self.training_classes.append(image)
        trainfile.close()

        testfile = open(testfile_name, 'r')
        for line in testfile:
            if len(line) < 32:
                for ch in line:
                    if ch.isdigit():
                        self.testing_labels.append(int(ch))
        testfile.seek(0) 
        for label in self.testing_labels:
            image = []
            for i in range(32):
                image_line = testfile.readline()
                for j in range(32):
                    image.append(image_line[j])
            image_line = testfile.readline()
            for ch in image_line:
                if ch.isdigit() and int(ch) != label:
                    print('TESTFILE ALIGN ERROR')
            self.testing_classes.append(image)
        testfile.close()

    # Make a prediction with weights
    def predict(self, row, weights):
        activation = weights[-1]
        for i in range(len(row) - 1):
            activation += weights[i] * row[i]
        return 1 if activation >= 0 else 0

    def train_weights(self, training_data, target_labels, learning_rate, num_epoch):
        for label in range(10):
            data_set = []
            for idx in range(len(training_data)):
                if label == target_labels[idx]:
                    row = training_data[idx] + [1]
                else:
                    row = training_data[idx] + [0]
                data_set.append(row)
            for epoch in range(num_epoch):
                total_error = 0
                for row in data_set:
                    prediction = self.predict(row, self.weight_list[label])
                    error = row[-1] - prediction
                    total_error += error**2
                    self.weight_list[label][-1] = self.weight_list[label][-1] + learning_rate*error
                    for i in range(len(row) - 1):
                        self.weight_list[label][i] = self.weight_list[label][i] + learning_rate*error*row[i]
                print('epoch #%d, learning_rate = %.3f, error = %.3f' %(epoch, learning_rate, total_error))
                print(self.weight_list[label])

    def perceptron_training(self, learning_rate, num_epoch):
        self.train_weights(self.training_classes, self.training_labels, learning_rate, num_epoch)

