import numpy as np
from nn.activation import stringToFunction

class Layer:

    def __init__( self, neurons, activation, bias_min, bias_max ):

        # Neurons
        self.neurons = neurons

        # Biases
        self.bias_max = bias_max
        self.bias_min = bias_min
        self.bias_range = bias_max - bias_min
        self.biases = np.random.uniform(self.bias_min, self.bias_max, neurons)

        # Activation function
        self.activation = activation






class FeedForwardNetwork:

    fitness = 0

    def __init__( self, layer_sizes : list, config ):

        self.config = config
        
        # Create layers based off of config
        self.layers = []
        for layer_size in layer_sizes:

            activation = stringToFunction[self.config['activation_default']]
            min_bias = self.config['bias_min']
            max_bias = self.config['bias_max']

            self.layers.append( Layer(layer_size, activation, min_bias, max_bias) )


        # Create weight Matrices
        self.weights = []
        for i, layer in enumerate(self.layers):

            min_weight = self.config['weight_min']
            max_weight = self.config['weight_max']

            if i == 0:
                self.weights.append(np.random.uniform(min_weight, max_weight, (layer.neurons, layer.neurons)))
            else:
                previous_layer_size = self.layers[i-1].neurons
                self.weights.append(np.random.uniform(min_weight, max_weight, (previous_layer_size, layer.neurons)))

    def reset_fitness( self ) -> None:
        self.fitness = 0


    def predict( self, inputs : np.array ):

        values = inputs

        for i, layer in enumerate(self.layers):

            aggregations = np.dot(values, self.weights[i])
            

            # add Biases
            biased = aggregations + layer.biases

            # Apply activations
            activated = np.array(list(map(layer.activation, biased)))

            values = activated

        return values
