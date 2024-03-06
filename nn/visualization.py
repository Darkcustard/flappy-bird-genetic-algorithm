from nn.network import FeedForwardNetwork
from pygame import Surface
from pygame import draw








def visualize( window : Surface, network : FeedForwardNetwork, origin : tuple[int, int] ):

    max_weight_thickness = 5
    min_weight_thickness = 0

    negative_weight_color = (255,0,0)
    positive_weight_color = (0,255,0)

    node_radius = 5
    node_color = (175,175,175)
    node_col_spacing = 10
    node_row_spacing = 10

    # Calculate distances etc.
    diagram_height = max([len(layer.biases) for layer in network.layers])*node_radius*2*node_row_spacing + node_row_spacing
    print(diagram_height)

    # Draw weights
    


    



