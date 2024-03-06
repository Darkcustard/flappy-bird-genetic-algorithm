from nn.network import FeedForwardNetwork
from nn.config_parser import parse_config
from nn.activation import stringToFunction
from random import shuffle, random, choice
from copy import deepcopy
from math import ceil
from time import time

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

            print(f"Beginning generation : {x}")
            print("---------------------------------")
            starttime = time()

            # Reset network fitnesses
            [net.reset_fitness() for net in self.networks]
            
            # Eval networks
            evaluator_function( self.networks )

            # Shuffle networks
            shuffle(self.networks)

            # Rank networks
            self.networks.sort( reverse = True, key = lambda x : x.fitness )
            fitnesses = [net.fitness for net in self.networks]
            bestfitness = fitnesses[0]
            avgfitness = sum(fitnesses)/len(fitnesses)
            print(f"Best fitness : {bestfitness}")
            print(f"Average fitness : {avgfitness}")
            
            
            # kill n networks
            survivor_count = round(self.config['survival_threshhold']*self.config['population_size'])
            reproduction_quota = len(self.networks)-survivor_count
            self.networks = self.networks[0:survivor_count]

            # Refresh networks
            for i in range(survivor_count):

                # Calculate how many copies to make
                copycount = -((2*reproduction_quota*i)/(survivor_count*(1-self.config['elitist_reproduction_coefficient']))**2) + ((2*reproduction_quota)/(survivor_count*(1-self.config['elitist_reproduction_coefficient'])))
                copycount = ceil(self.clamp(copycount, 0, self.config['population_size']))

                for x in range(copycount):

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

                            # Replace Biases
                            if self.odds( self.config['bias_replace_rate'] ):

                                new_bias = (self.config['bias_max'] - self.config['bias_min'])*random() + self.config['bias_min']
                                copy.layers[ldx].biases[bdx] = new_bias

                        if self.odds( self.config['activation_mutate_rate']):
                            layer.activation = stringToFunction[choice(self.config['activation_options'])]
    
                    self.networks.append(copy)
                
            endtime = time()
            self.networks = self.networks[0:int(self.config['population_size'])]
            print(f"Generation finished in : {round((endtime-starttime)*10)/10} seconds. \n")

        return self.networks[0]