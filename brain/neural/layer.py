from brain.neural.neuron import Neuron


class Layer:

    def __init__(self, neurons, inputs):

        self.neurons = [

            Neuron(inputs)

            for _ in range(neurons)

        ]

    def forward(self, values):

        outputs = []

        for neuron in self.neurons:

            outputs.append(
                neuron.forward(values)
            )

        return outputs
