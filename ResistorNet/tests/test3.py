from src.lib import Network,Resistor,Node
from src.lib.finder import find_series,find_parallels
from src.lib.combine import combine_all_serieses,combine_all_parallels
from src.lib.update_network import network_updater

net = Network()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')
h = Node('H')

r1 = Resistor('R1',1000,a,f)
r2 = Resistor('R2',500,b,f)
r3 = Resistor('R3',300,g,b)
r4 = Resistor('R4',300,g,h)
r5 = Resistor('R5',200,h,c)
r6 = Resistor('R6',1000,b,d)
r7 = Resistor('R7',1000,d,b)
r8 = Resistor('R7',100,b,e)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)
net.add_resistor(r4)
net.add_resistor(r5)
net.add_resistor(r6)
net.add_resistor(r7)
net.add_resistor(r8)

net.set_ground(c)
net.set_ground(d)
net.set_ground(a)
net.set_ground(e)

combine_all_serieses(net,find_series(net))
combine_all_parallels(net,find_parallels(net))
network_updater(net)

net.print_resistors()