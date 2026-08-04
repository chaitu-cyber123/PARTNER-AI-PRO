from brain.neural.layer import Layer
from brain.neural.activation import sigmoid


class Network:

    def __init__(self):

        self.hidden = Layer(
            neurons=4,
            inputs=3
        )

        self.output = Layer(
            neurons=2,
            inputs=4
        )

    def predict(self, values):

        hidden = self.hidden.forward(values)

        hidden = [

            sigmoid(x)

            for x in hidden

        ]

        output = self.output.forward(hidden)

        output = [

            sigmoid(x)

            for x in output

        ]

        return output
