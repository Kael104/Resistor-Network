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

r1 = Resistor('R1',100,a,b)
r2 = Resistor('R2',100,a,b)
r3 = Resistor('R3',200,a,c)
r4 = Resistor('R4',200,c,e)
r5 = Resistor('R5',300,e,d)
r6 = Resistor('R6',300,e,d)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)
net.add_resistor(r4)
net.add_resistor(r5)
net.add_resistor(r6)

net.set_ground(b)
net.set_ground(d)



combine_all_serieses(net,find_series(net))
combine_all_parallels(net,find_parallels(net))
network_updater(net)
combine_all_serieses(net,find_series(net))

net.print_resistors()
