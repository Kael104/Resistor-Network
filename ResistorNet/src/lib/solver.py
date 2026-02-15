from .network import Network
from .resistor import Resistor
from .finder import find_parallels, find_series
from .combine import combine_all_parallels, combine_all_serieses
from .update_network import network_updater
from .visualizer import visualize_graph
import matplotlib.pyplot as plt

def check_if_star(network:Network):
    nodes = list(network.get_nodes())
    not_ground = 0
    ref = None
    for node in nodes:
        if not node.is_ground:
            ref = node
            not_ground += 1
        if not_ground > 1:
            return False
    for res in network.resistors:
        if not res.is_connected(ref):
            return False
        else:
            if not res.get_other_node(ref).is_ground:
                return False
    return True
def node_resistance(network: Network) -> float:
    if not network.resistors:
        raise ValueError("No resistors in the network")

    plt.ion()
    fig, ax = plt.subplots(figsize=(8, 8))

    step = -1
    while True:

        parallels = find_parallels(network)
        series = find_series(network)

        if not parallels and not series:
            step += 1
            fig, ax = visualize_graph(network, fig_ax=(fig, ax))
            ax.set_title(f"Reduction Step {step}", fontsize=14)
            plt.pause(4)  
            break

        step += 1
        fig, ax = visualize_graph(network, fig_ax=(fig, ax))
        if step == 0:
            ax.set_title(f"Original Circuit", fontsize=14)
            plt.pause(4) 
        else: 
            ax.set_title(f"Reduction Step {step}", fontsize=14)
            plt.pause(4)  

        if parallels:
            combine_all_parallels(network, parallels)
        if series:
            combine_all_serieses(network, series)
        network_updater(network)
    
    if check_if_star(network):
        nodes = [node for node in network.nodes if node.is_ground]
        x = nodes[0]
        y = nodes[1]
        tot = 0
        for res in network.resistors:
            tot += 1.0/res.resistance
        tot = 1.0/tot
        network.clear_network()
        network.add_resistor(Resistor('R1',tot,x,y))
        network_updater(network)
    fig, ax = visualize_graph(network, fig_ax=(fig, ax))
    ax.set_title("Final Reduced Network", fontsize=14)
    plt.pause(1.5)

    plt.ioff()
    plt.show()  

    return network.resistors[0]
