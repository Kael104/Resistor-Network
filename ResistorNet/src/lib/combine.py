from .network import Network
from .resistor import Resistor

def combine_all_parallels(network:Network,parallels):
    for pargroup in parallels:
        combine_parallel(network,pargroup)

def combine_parallel(network:Network,parallel_group:list[Resistor]):
    ref = parallel_group[0]
    temp = 0
    for res in parallel_group:
        temp += 1.0/res.resistance
        if res != ref:
            network.disconnect_resistor(res)
    equivalent = 1.0/temp if temp != 0 else 0
    ref.resistance = equivalent

def combine_all_serieses(network:Network,serieses):
    for seriesgroup in serieses:
        combine_series(network,seriesgroup)

def combine_series(network:Network,seriesgroup:list[Resistor]):
    ref1 = seriesgroup[0]
    ref2 = seriesgroup[-1]
    
    rnode = ref1.node1 if ref1.node1.is_ground or len(ref1.node1.get_connected()) > 2 else ref1.node2
    lnode = ref2.node1 if ref2.node1.is_ground or len(ref2.node1.get_connected()) > 2 else ref2.node2
    
    equiv = 0
    for res in seriesgroup:
        equiv += res.resistance
        if res != ref1:
            network.disconnect_resistor(res)
    ref1.connect_node1(lnode)
    ref1.connect_node2(rnode)

    if ref1.node1 == lnode:
        ref1.connect_node2(rnode)
    elif ref1.node2 == lnode:
        ref1.connect_node1(rnode)
    elif ref1.node1 == rnode:
        ref1.connect_node2(lnode)
    else:
        ref1.connect_node1(lnode)
    ref1.resistance = equiv
