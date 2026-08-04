import random


class Neuron:

    def __init__(self, inputs):

        self.weights = [
            random.uniform(-1, 1)
            for _ in range(inputs)
        ]

        self.bias = random.uniform(-1, 1)

    def forward(self, values):

        total = self.bias

        for w, x in zip(self.weights, values):
            total += w * x

        return total
