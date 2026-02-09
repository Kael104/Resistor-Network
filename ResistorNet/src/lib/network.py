class Network():
    def __init__(self):
        self.resistors = []
        self.nodes = set()
    def add_resistor(self,resistor):
        if resistor not in self.resistors:
            self.resistors.append(resistor)
        node1 = resistor.node1
        node2 = resistor.node2

        node1.connect_to_node(resistor)
        node2.connect_to_node(resistor)

        if node1 not in self.nodes:
            self.nodes.add(node1)
        if node2 not in self.nodes:
            self.nodes.add(node2)
    def set_ground(self,node):
        node.set_to_ground()
    def disconnect_resistor(self,resistor):
        if resistor in self.resistors:
            resistor.node1.disconnect_resistor(resistor)
            resistor.node2.disconnect_resistor(resistor)
            self.resistors.remove(resistor)
    def remove_node(self,node):
        if node in self.nodes:
            self.nodes.remove(node)
    def get_resistors(self):
        return self.resistors
    def get_nodes(self):
        return self.nodes
    def print_resistors(self):
        for res in self.resistors:
            print(res)
    def print_nodes(self):
        for node in self.nodes:
            print(node.print_connected())
    def clear_network(self):
        self.resistors = []
        self.nodes = set()