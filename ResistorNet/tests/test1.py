from src.lib.network import Network
from src.lib.resistor import Resistor
from src.lib.node import Node

net = Network()

a = Node('A')
b = Node('B')
c = Node('C')

r1 = Resistor('R1',500,a,b)
r2 = Resistor('R2',1000,b,c)

net.add_resistor(r1)
net.add_resistor(r2)

for node in net.get_nodes():
    print(node.name, [(res.name,res.resistance) for res in node.get_connected()])

for res in net.get_resistors():
    print(res.name,res.resistance, res.node1.name, res.node2.name)