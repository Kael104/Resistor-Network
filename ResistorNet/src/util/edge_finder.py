from ..lib import Network, Node, Resistor

def find_edges(network:Network):
    edges = []
    seen = []
    for res in network.get_resistors():
        nodes = set([res.node1,res.node2])
        if nodes not in seen:
            seen.append(nodes)
            edges.append((res.node1,res.node2))
    return edges