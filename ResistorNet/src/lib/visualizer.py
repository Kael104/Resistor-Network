from .network import Network
import matplotlib.pyplot as plt
import networkx as nx

def make_graph(net:Network):
    graph = nx.MultiGraph()

    for node in net.nodes:
        graph.add_node(node.name)
    for resistor in net.resistors:
        graph.add_edge(resistor.node1.name,resistor.node2.name,label = resistor.name ,weight = resistor.resistance)
    return graph

def visualize_graph(net: Network):
    ref_node = {node.name:node for node in net.nodes}

    graph = make_graph(net)
    pos = nx.kamada_kawai_layout(graph,scale=10.0,weight=None)

    plt.figure(figsize=(8,8))

    node_colors = ['black' if ref_node[node].is_ground else 'brown' for node in graph.nodes()]
    nx.set_node_attributes(graph,dict(zip(graph.nodes,node_colors)),'color')
    nx.draw_networkx_nodes(graph, pos, node_size=300, node_color=[graph.nodes[node]['color'] for node in graph.nodes()])
    
    nx.draw_networkx_edges(graph, pos, width=1)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold', font_color= 'white')
    edge_labels = nx.get_edge_attributes(graph, 'weight') 

    edge_labels = {res: f"{resistance}Ω" for res, resistance in edge_labels.items()}
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels, font_color='red',font_size=8)

    plt.margins(0.2)

    plt.axis('off')
    plt.show()
