from Node import Node
from Link import Link
from Packet import Packet


node1 = Node(node_id=1, address="00:01")
node2 = Node(node_id=2, address="00:02")
link = Link(node1, node2)

packet = Packet(source=node1.address, destination=node2.address, payload="Hello world")
node1.send_packet(packet)