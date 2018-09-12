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
        policy = np.array(temp_list)
        states = policy[:, :5]
        norm_state = self.normalize(states)
        actions = policy[:, 5:6]
        self.expert_policy = np.zeros((len(states), 6))
        for i in range(len(states)):
            for j in range(5):
                self.expert_policy[i][j] = norm_state[i][j]
            self.expert_policy[i][5] = actions[i][0]
        self.expert_states = self.expert_policy[:, :5]
        self.expert_actions = self.expert_policy[:, 5:6]
        
    def normalize(self, arr):
        arr_T = arr.T
        new_arr = []
        for row in arr_T:
            mean = row.sum()/len(row)
            std = np.std(row)
            new_row = []
            for i in range(len(row)):
                elem = (row[i]-mean)/std
                new_row.append(elem)
            new_arr.append(new_row)
        return np.array(new_arr).T

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
            y_i = int(y[i])
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

    def three_layer_network(self, X, weights, biases, y, test):
        W1, W2, W3 = weights
        b1, b2, b3 = biases

        Z1, acache1 = self.affine_forward(X, W1, b1)
        A1, rcache1 = self.relu_forward(Z1)
        Z2, acache2 = self.affine_forward(A1, W2, b2)
        A2, rcache2 = self.relu_forward(Z2)
        F, acache3 = self.affine_forward(A2, W3, b3)

        if test == True:
            n, _ = np.shape(F)
            classifications = np.zeros((n, ))
            for i in range(n):
                classifications[i] = max(F[i])
            return classifications

        loss, dF = self.cross_entropy(F, y)
        dA2, dW3, db3 = self.affine_backward(dF, acache3)
        dZ2 = self.relu_backward(dA2, rcache2)
        dA1, dW2, db2 = self.affine_backward(dZ2, acache2)
        dZ1 = self.relu_backward(dA1, rcache1)
        dX, dW1, db1 = self.affine_backward(dZ1, acache1)

        mu = 0.1
        W1 = W1 - mu*dW1
        W2 = W2 - mu*dW2
        W3 = W3 - mu*dW3
        b1 = b1 - mu*db1
        b2 = b2 - mu*db2
        b3 = b3 - mu*db3
        updated_weights = (W1, W2, W3)
        updated_biases = (b1, b2, b3)
        return loss, updated_weights, updated_biases

    def minibatch(self, data, epoch, batch_size, feature_size, test):
        n, d = np.shape(data)
        weights, biases = self.init_wb(d-1, feature_size)
        loss_list = []
        for e in range(epoch):
            np.random.shuffle(data)
            num_batch = int(n / batch_size)
            total_loss = 0
            for i in range(num_batch):
                X, y = self.get_batch(data, batch_size, i)
                loss, weights, biases = self.three_layer_network(X, weights, biases, y, test)
                total_loss += loss
                print('Epoch: %d, Batch: %d, Loss: %.5f' %(e, i, loss))
            print('Total Loss: %.5f' %(total_loss/num_batch))
            loss_list.append(total_loss/num_batch)
        loss_list = np.array(loss_list)
        return weights, biases, loss_list

    
    def train(self):
        self.weights, self.biases, loss_list = self.minibatch(self.expert_policy, 100, 100, 64, False)
        return loss_list

    def test(self):
        classifications = self.three_layer_network(self.expert_policy, self.weights, self.biases, self.expert_actions, True)



    def get_batch(self, data, size, index):
        start = index * size
        end = start + size
        data_b = data[start:end, :]
        X = data_b[:, 0:5]
        y = data_b[:, 5:6]
        return X, y

    def init_wb(self, d, f):
        W1 = np.random.randn(d, f)*0.1
        W2 = np.random.randn(f, f)*0.1
        W3 = np.random.randn(f, 3)*0.1
        b1 = np.random.randn(f)
        b2 = np.random.randn(f)
        b3 = np.random.randn(3)
        weights = (W1, W2, W3)
        biases = (b1, b2, b3)
        return weights, biases
