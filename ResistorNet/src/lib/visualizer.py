from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
from .network import Network

def make_graph(net: Network):
    graph = nx.MultiGraph()
    for node in net.nodes:
        graph.add_node(node.name)
    for resistor in net.resistors:
        graph.add_edge(resistor.node1.name, resistor.node2.name, label=resistor.name, weight=resistor.resistance)
    return graph

def visualize_graph(net: Network, fig_ax=None):
    if fig_ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))
    else:
        fig, ax = fig_ax
        ax.clear()

    graph = make_graph(net)
    pos = nx.kamada_kawai_layout(graph, scale=10.0, weight=None)

    node_colors = ['black' if node.is_ground else 'brown' for node in net.nodes]
    nx.draw_networkx_nodes(graph, pos, node_size=300, node_color=node_colors, ax=ax)
    nx.draw_networkx_labels(graph, pos, font_size=10, font_weight='bold', font_color='white', ax=ax)
    nx.draw_networkx_edges(graph, pos, width=1, ax=ax)

    edge_groups = defaultdict(list)
    for u, v, key, data in graph.edges(keys=True, data=True):
        pair = tuple(sorted((u, v)))
        edge_groups[pair].append(data['weight'])

    for (u, v), weights in edge_groups.items():
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        mid_x = (x1 + x2) / 2
        mid_y = (y1 + y2) / 2
        for i, w in enumerate(weights):
            offset_index = i - (len(weights)-1)/2
            ax.text(mid_x, mid_y + 0.6*offset_index, f"{w}Ω", fontsize=8, color='red',
                    ha='center', va='center', bbox=dict(facecolor='white', edgecolor='none', alpha=0.3))

    ax.set_axis_off()
    plt.draw()
    return fig, ax
