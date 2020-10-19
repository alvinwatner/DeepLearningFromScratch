from Layer import Layer
import numpy as np

class Sequential:
    def __init__(self):
        self.graph = {}

    def __repr__(self):
        for layer in self.graph:
            print(layer)

    def add(self, num_neuron = None, input_shape = None, activation = 'linear'):

        if len(self.graph) == 0:
            if input_shape == None:
                raise Exception("Please specify input_shape for the input layer")
            else:
                layer = Layer(num_neuron, input_shape)
        else:
            layer = Layer(num_neuron, activation)
            weight = self.create_Weights()
            self.graph['weights'].append(weight)

        self.graph['layer'].append(layer)

    def create_Weights(self):
        vector_dim = len(self.graph['layer'][-2])
        vector_space = len(self.graph['layer'][-1])
        return np.random.random((vector_space, vector_dim))

    def predict(self, vector_inp):
        num_weights = len(self.graph['weights'])
        num_inputNeuron = len(vector_inp)
        for i in range(num_weights):
            out = np.matmul(self.graph['weights'][i], vector_inp)
            out = ac


    def fit(self, x, y):
        pass

