import numpy as np
import numpy.linalg as la
from math import log, exp

class Cloning:
    def __init__(self, source):
        self.parse_policy(source)

    def parse_policy(self, source):
        source_file = open(source, 'r')
        temp_list = []
        for line in source_file:
            tokens = line.split(' ')
            line_list = [float(num) for num in tokens]
            temp_list.append(line_list)
        source_file.close()
        self.expert_policy = np.array(temp_list)
        self.expert_states = self.expert_policy[:, :5]
        self.expert_actions = self.expert_policy[:, 5:6]

    def affine_forward(self, A, W, b):
        Z = A@W + b
        return Z, (A, W, b)

    def affine_backward(self, dZ, cache):
        A, W, b = cache

        n = np.shape(A)[0]
        d = np.shape(W)[0]
        dp = np.shape(b)[0]

        dA = np.zeros((n, d))
        dW = np.zeros((d, dp))
        db = np.zeros((dp, ))

        for i in range(n):
            for k in range(d):
                for j in range(dp):
                    dA[i][k] += dZ[i][j]*W[k][j]
                    dW[k][j] += A[i][k]*dZ[i][j]
        for j in range(dp):
            for i in range(n):
                db[j] += dZ[i][j]
        return dA, dW, db

    def relu_forward(self, Z):
        n, dp = np.shape(Z)
        A = np.zeros((n, dp))
        for i in range(n):
            for j in range(dp):
                if Z[i][j] > 0:
                    A[i][j] = Z[i][j]
        return A, Z

    def relu_backward(self, dA, cache):
        Z = cache
        n, dp = np.shape(dA)
        dZ = np.zeros((n, dp))
        for i in range(n):
            for j in range(dp):
                if Z[i][j] > 0:
                    dZ[i][j] = dA[i][j]
        return dZ

    def cross_entropy(self, F, y):
        n, _ = np.shape(F)
        L = 0

        for i in range(n):
            loc_sum = 0
            for j in range(3):
                loc_sum += exp(F[i][j])
            y_i = y[i]
            L += F[i][y_i] - log(loc_sum)
        L = -L/n

        dF = np.zeros((n, 3))
        for i in range(n):
            for j in range(3):
                indicater = 1 if j == y[i] else 0
                loc_sum = 0
                for k in range(3):
                    loc_sum += exp(F[i][k])
                dF[i][j] = -(indicater - exp(F[i][j])/loc_sum)/n
        return L, dF

