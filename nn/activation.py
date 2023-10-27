from math import e

def relu ( x : float ) -> float:

    if x > 0.0:
        return x
    return 0.0

def leaky_relu ( x : float ) -> float:

    sigma = 0.2
    if x > 0.0:
        return x
    else:
        return sigma*x
    
def sigmoid ( x : float ) -> float:

    if x > 0:
        return 1 / (1 + e**-x)
    else:
        return e**x/(1+e**x)

def tanh ( x : float ) -> float:

    return sigmoid(x)*2-1


stringToFunction = {

    'relu' : relu,
    'leaky_relu' : leaky_relu,
    'sigmoid' : sigmoid,
    'tanh' : tanh,

}
    
