class Node:
    def __init__(self, node_id, address=None):
        self.node_id = node_id
        self.address = address
        self.links = []
    
    def add_link(self, link):
        if link not in self.links:
            self.links.append(link)

    def send_packet(self, packet):
        if packet.destination == self.address:
            self.receive_packet(packet)
        else:
            for link in self.links:
                next_node = link.node_x if self != link.node_x else link.node_y
                print(f"ノード{self.node_id}からノード{next_node.node_id}へパケットを転送")
                link.transfer_packet(packet, self)
                break

    def receive_packet(self, packet):
        print(f"ノード{self.node_id}がパケットを受信: {packet.payload}")

    def __str__(self):
        connected = [link.node_y.node_id if self == link.node_x else link.node_x.node_id for link in self.links]
        return f"ノード(ID: {self.node_id}, アドレス: {self.address}, 接続: {connected})"
        