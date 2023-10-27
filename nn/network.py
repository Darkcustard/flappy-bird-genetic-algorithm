import numpy as np
from config_parser import parse_config
from activation import stringToFunction

class Layer:

    def __init__( self, neurons, activation, bias_min, bias_max ):

        # Neurons
        self.neurons = neurons

        # Biases
        self.bias_max = bias_max
        self.bias_min = bias_min
        self.bias_range = bias_max - bias_min
        self.biases = np.random.rand(neurons)*self.bias_range + np.full(neurons, self.bias_min)

        # Activation function
        self.activation = activation



class FeedForwardNetwork:

    def __init__( self, layer_sizes : list, config_path ):

        self.config = parse_config(config_path)
        

        # Create layers based off of config
        self.layers = []
        for layer_size in layer_sizes:

            activation = stringToFunction[self.config['activation_default']]
            min_bias = self.config['bias_min']
            max_bias = self.config['bias_max']

            self.layers.append( Layer(layer_sizes, activation, min_bias, max_bias) )


        # Create weight Matrices
        for i, layer in enumerate(self.layers):

            if i == 0:
                pass



