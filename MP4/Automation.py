import subprocess
from jsonpickle import decode, encode
import numpy as np
import os

def find(dir, file):
    for root, dir, files in os.walk(dir):
        if file in files:
            return True
    return False

def create_record(c, gamma, ne, result):  # give the set of paremters output the record object
    return {'c': c, 'gamma': gamma, 'ne': ne, 'avg': result}


def read_file(directory, filename):  # return the entire object
    if find(directory, filename):
        with open(directory + filename, 'r') as f:
            training = f.read()
            return decode(training)
    else:
        return []
def store_result(obj, record, directory, filename):  # given object and file
    obj.append(record)
    training_result = encode(obj)
    with open(directory + filename, 'w') as f:
        f.write(training_result)


def store_training_result(directory, filename, c, gamma, ne, result):
    record = create_record(c, gamma, ne, result)
    obj = read_file(directory, filename)
    store_result(obj, record, directory, filename)

def main():
#    for C in [10, 20, 30]:
#        for GAMMA in [0.4, 0.7, 0.9]:
#            for NE in [50, 100, 150]:
#                subprocess.call(['python3', 'pong.py', '--c', str(C), '--gamma', str(GAMMA), '--ne', str(NE), '--train', str(1)])
#                subprocess.call(['python3', 'pong.py', '--c', str(C), '--gamma', str(GAMMA), '--ne', str(NE)])

    for c in [15, 25, 35]:
        for gamma in [0.4, 0.7, 0.9]:
            for ne in [50, 100, 150]:
                subprocess.call(['python3', 'pong.py', '--c', str(c), '--gamma', str(gamma), '--ne', str(ne), '--train', str(1)])
                subprocess.call(['python3', 'pong.py', '--c', str(c), '--gamma', str(gamma), '--ne', str(ne)])

