from src.lib import Network,Resistor,Node
from src.lib.finder import find_parallels
from src.lib.combine import combine_all_parallels
from src.lib.solver import node_resistance
from src.lib.visualizer import visualize_graph
net = Network()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')

r1 = Resistor('R1',100,a,b)
r2 = Resistor('R2',100,b,c)
r3 = Resistor('R3',100,b,c)
r4 = Resistor('R4',100,c,d)
r5 = Resistor('R5',100,c,e)


net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)
net.add_resistor(r4)
net.add_resistor(r5)

net.set_ground(d)
net.set_ground(a)
net.set_ground(e)

print(node_resistance(net))