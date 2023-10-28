from nn.network import FeedForwardNetwork
from nn.config_parser import parse_config
from random import shuffle, random
from copy import deepcopy
from math import ceil

class Population:

    def __init__(self, network_shape,  config_path):

        self.config = parse_config(config_path)
        self.networks = []

        for x in range(int(self.config['population_size'])):
            self.networks.append(FeedForwardNetwork(network_shape, self.config))


    def odds ( self, x ) -> bool:

        if random() <= x:
            return True
        return True
    
    def clamp ( self, x, minimum, maximum ) -> float:

        if x < minimum:
            return minimum
        elif x > maximum:
            return maximum
        return x


    def fit ( self, evaluator_function, generations ) -> FeedForwardNetwork:

        for x in range(generations):

            # Reset network fitnesses
            [net.reset_fitness() for net in self.networks]

            # Shuffle networks
            shuffle(self.networks)

            # Rank networks
            self.networks.sort( reverse = True, key = lambda x : x.fitness )
            
            # kill n networks
            survivor_count = round(self.config['survival_threshhold']*self.config['population_size'])
            self.networks = self.networks[0:survivor_count]

            # Refresh networks
            i = 0
            while len(self.networks) < self.config['population_size']:

                copy = deepcopy( self.networks[i] )

                # Mutate Weights
                for wmdx, weight_matrix in enumerate( copy.weights ):
                    for bmdx, bias_matrix in enumerate( weight_matrix ):
                        for wdx, weight in enumerate( bias_matrix ):
                            
                            # Mutate Rate
                            if self.odds( self.config['weight_mutate_rate'] ):
                                
                                mutation_factor = self.config['weight_mutate_power'] * (random()*2-1)
                                new_weight = weight + mutation_factor
                                new_weight = self.clamp(new_weight, self.config['weight_min'], self.config['weight_max'])
                                copy.weights[wmdx][bmdx][wdx] = new_weight

                            # Replace Rate
                            if self.odds( self.config['weight_replace_rate'] ):

                                new_weight = (self.config['weight_max'] - self.config['weight_min'])*random() + self.config['weight_min']
                                copy.weights[wmdx][bmdx][wdx] = new_weight

                # Mutate Biases
                for ldx, layer in enumerate( copy.layers ):
                    for bdx, bias in enumerate( layer.biases ):
                        
                        # Mutate Bias
                        if self.odds( self.config['bias_mutate_rate'] ):

                            mutation_factor = self.config['bias_mutate_power'] * (random()*2-1)
                            new_bias = bias + mutation_factor
                            new_bias = self.clamp(new_bias, self.config['bias_min'], self.config['bias_max'])
                            copy.layers[ldx].biases[bdx] = new_bias

                        # Replace Bia
                        if self.odds( self.config['bias_replace_rate'] ):

                            new_bias = (self.config['bias_max'] - self.config['bias_min'])*random() + self.config['bias_min']
                            copy.layers[ldx].biases[bdx] = new_bias
   
                self.networks.append(copy)
                
                
                i += 1
                if i > survivor_count-1:
                    i = 0

        return self.networks[0]