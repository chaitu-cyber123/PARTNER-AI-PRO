from brain.neural.neuron import Neuron
from brain.neural.activation import sigmoid

n = Neuron(3)

inputs = [1, 0.5, -1]

output = n.forward(inputs)

print("Raw:", output)
print("Sigmoid:", sigmoid(output))
