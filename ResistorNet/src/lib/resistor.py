class Resistor():
    def __init__(self,name,resistance = 0,node1 = None,node2 = None):
        self.name = name
        self.resistance = resistance
        self.node1 = node1
        self.node2 = node2
    def __str__(self):
        return f"Resistor {self.name} with resistance {self.resistance} connected to {self.node1} and {self.node2}"
    def connect_node1(self,node):
        self.node1 = node
        node.connect_to_node(self)
    def connect_node2(self,node):
        self.node2 = node
        node.connect_to_node(self)
    def get_other_node(self,node):
        return self.node2 if self.node1 == node else self.node1
