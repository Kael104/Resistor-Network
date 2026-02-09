from src.lib import Network,Resistor,Node
from src.lib.finder import find_series,find_parallels
from src.lib.combine import combine_all_serieses,combine_all_parallels
net = Network()

a = Node('A')
b = Node('B')
d = Node('D')
e = Node('E')

r1 = Resistor('R1',50,a,b)
r2 = Resistor('R2',400,a,e)
r3 = Resistor('R3',150,e,d)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)

net.set_ground(b)
net.set_ground(d)

net.print_resistors()

net.print_nodes()
