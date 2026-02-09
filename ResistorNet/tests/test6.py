from src.lib import Network,Resistor,Node
from src.lib.finder import find_series,find_parallels
from src.lib.combine import combine_all_serieses,combine_all_parallels
from src.lib.update_network import network_updater
net = Network()

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')


r1 = Resistor('R1',100,a,b)
r2 = Resistor('R2',200,b,c)
r3 = Resistor('R3',300,c,d)

net.add_resistor(r1)
net.add_resistor(r2)
net.add_resistor(r3)

net.set_ground(a)
net.set_ground(d)

net.print_nodes()
net.print_resistors()
print("~~~~~~")

network_updater(net)
net.print_nodes()
net.print_resistors()
# so = find_series(net)
# for si in so:
#     for res in si:
#         print(res.resistance)
#     print('')

# combine_all_serieses(net,find_series(net))
# print(' ')
# net.print_nodes()
# net.print_resistors()