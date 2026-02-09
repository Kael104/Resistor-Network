from .network import Network
from .node import Node
from .resistor import Resistor
from .finder import find_parallels,find_series
from .combine import combine_all_parallels, combine_all_serieses, combine_parallel
from .update_network import network_updater

def check_if_simplified(network:Network) -> bool:
    if find_parallels(network):
        return False
    if find_series(network):
        return False
    return True
def node_resistance(network:Network, node:Node) -> float: # transform the network into node -> combined resistance -> GND
    if not network.resistors:
        raise ValueError('no resistors in net')
    while not check_if_simplified(network):
        combine_all_parallels(network,find_parallels(network))
        combine_all_serieses(network,find_series(network))
        network_updater(network)
    equiv = 0
    for res in network.resistors:
        if res.resistance == 0:
            continue
        equiv += 1.0/res.resistance
    return 1.0/equiv if equiv else 0
