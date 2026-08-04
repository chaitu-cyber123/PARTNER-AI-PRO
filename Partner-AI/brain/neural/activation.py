import math


def sigmoid(x):

    return 1 / (1 + math.exp(-x))


def relu(x):

    if x > 0:
        return x

    return 0
