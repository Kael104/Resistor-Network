from src.lib import Network, Resistor, Node
from src.lib.finder import find_series, find_parallels
from src.lib.combine import combine_all_serieses, combine_all_parallels
from src.lib.update_network import network_updater
from src.lib.visualizer import visualize_graph, make_graph
from src.lib.solver import node_resistance

net = Network()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

r1 = Resistor('R1',200,b,f)
r2 = Resistor('R2',200,b,f)
r3 = Resistor('R3',200,d,b)
r4 = Resistor('R4',200,b,d)
r5 = Resistor('R5',500,a,b)
r6 = Resistor('R6',1000,b,c)
r7 = Resistor('R7',300,d,e)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)
net.add_resistor(r4)
net.add_resistor(r5)
net.add_resistor(r6)
net.add_resistor(r7)

net.set_ground(c)
net.set_ground(f)
net.set_ground(a)
net.set_ground(e)

print("Equivalent resistance at node A:", node_resistance(net))
