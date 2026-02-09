from src.lib import Network,Resistor,Node
from src.lib.finder import find_parallels
from src.lib.combine import combine_all_parallels
from src.lib.solver import node_resistance
net = Network()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')

r1 = Resistor('R1',100,a,f)
r2 = Resistor('R2',100,a,e)
r3 = Resistor('R3',100,e,f)
r4 = Resistor('R4',100,e,f)
r5 = Resistor('R5',100,a,b)
r6 = Resistor('R6',100,b,c)
r7 = Resistor('R7',100,c,d)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)
net.add_resistor(r4)
net.add_resistor(r5)
net.add_resistor(r6)
net.add_resistor(r7)

net.set_ground(d)
net.set_ground(e)

print (node_resistance(net,a))