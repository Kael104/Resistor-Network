from .network import Network

def network_updater(network:Network):
    resistor_storage = network.resistors.copy()
    network.clear_network()
    for res in resistor_storage:
        network.add_resistor(res)
    