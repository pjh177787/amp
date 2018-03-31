import numpy as np
import math

class Bayesian_Model:
    def __init__(self):
        self.classes = [
            [
                [{'1':0, '0':0} for i in range(32)]
                for i in range(32)]
            for i in range(10)]
        self.confusionMat = [[0 for i in range(10)] for i in range(10)]
        self.count = np.zeros(10) # count of appearances of each number in the training sample
        self.priors = np.zeros(10)

    def train(self, trainfile_name, smooth_factor):
        trainfile = open(trainfile_name, 'r')
        label_list = []
        for line in trainfile:
            if len(line) < 32:
                for ch in line:
                    if ch.isdigit():
                        label_list.append(ch)
        for label in label_list:
            self.count[label] += 1
            for i in range(32):
                image_line = trainfile.readline()
                for j in range(32):
                    self.classes[label][i][j][image_line[j]] += 1
        image_line = trainfile.readline()
        for ch in image_line:
            if ch.isdigit() and int(ch) != label:
                print('ALIGN ERROR')
        self.laplace_smooth(smooth_factor)

    def laplace_smooth(self, factor):
        for num in range(10):
            if self.count[num] > 0:
                denom = math.log2(self.count[num] + factor*2)
            else:
                denom = float('-inf')
            for i in range(32):
                for j in range(32):
                    for pixel in self.classes[num][i][j]:
                        self.classes[num][i][j][pixel] = math.log2(self.classes[num][i][j][pixel] + factor ) - denom
