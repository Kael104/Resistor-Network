import uuid
class Node():
    def __init__(self,name,connected = None):
        self.name = name
        self.connected = [] if connected is None else connected
        self.is_ground = False
        self.id = uuid.uuid4()
    def connect_to_node(self,resistor):
        if resistor not in self.connected:
            self.connected.append(resistor)
    def get_connected(self):
        return self.connected
    def set_to_ground(self):
        self.is_ground = True
    def disconnect_resistor(self,resistor):
        if resistor in self.connected:  
            self.connected.remove(resistor)
    def print_connected(self):
        resstring = ''
        for res in self.connected:
            resstring += f"{res.name} {res.resistance} "
        return f"{self.name} {'G' if self.is_ground else 'N'} {resstring}"

    def __str__(self):
        return f"{self.name}"
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.id == other.id
        return False
    def __hash__(self):
        return hash(self.id)
    