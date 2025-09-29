class Link:
    def __init__(self, node_x, node_y, bandwidth=10000, delay=0.001, packet_loss=0.0):
        self.node_x = node_x
        self.node_y = node_y
        self.bandwidth = bandwidth
        self.delay = delay
        self.packet_loss = packet_loss
        
        node_x.add_link(self)
        node_y.add_link(self)

    def transfer_packet(self, packet, from_node):
        next_node = self.node_x if from_node != self.node_x else self.node_y
        next_node.receive_packet(packet)

    def __str__(self):
        return f'リンク({self.node_x.node_id} ↔️  {self.node_y.node_id})、 帯域幅: {self.bandwidth}、遅延: {self.delay}、パケットロス率: {self.packet_loss}'