from .network import Network
from .node import Node
from ..util.edge_finder import find_edges

def find_parallels(network:Network):
    parallels = []
    edges = find_edges(network)
    for edge in edges:
        curr = []
        n1 = edge[0]
        n2 = edge[1]
        for res in n1.get_connected():
            if res.get_other_node(n1) == n2:
                curr.append(res)
        if len(curr) > 1:
            parallels.append(curr)
    return parallels

def find_series(network:Network):
    serieses = []
    seen = set()
    def dfs(node:Node,curr:list,prev = None):
        if prev:
            if node.is_ground or len(node.get_connected()) != 2:
                if len(curr) > 1:
                    serieses.append(curr.copy())
                return
            res1 = node.get_connected()[0]
            res2 = node.get_connected()[1]
            if res1 in seen or res2 in seen:
                nextresistor = res1 if res1 != prev else res2
                seen.add(nextresistor)
                curr.append(nextresistor)
                nextnode = nextresistor.get_other_node(node)
                dfs(nextnode,curr,nextresistor)
        else:
            for res in node.get_connected():
                if res not in seen:
                    curr = [res]
                    seen.add(res)
                    next_node = res.get_other_node(node)
                    dfs(next_node, curr, prev=res)
    for node in network.get_nodes():    
        if node.is_ground:
            dfs(node,[])
        if len(node.get_connected()) != 2:
            dfs(node,[])
    return serieses

