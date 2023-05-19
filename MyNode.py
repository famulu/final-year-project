import subprocess

from p2pnetwork.node import Node

class MyNode (Node):
    is_supernode = False

    def __init__(self, host, port, supernode_host: str, supernode_port: int, id=None, callback=None, max_connections=0):
        super().__init__(host, port, id, callback, max_connections)
        self.supernode_host = supernode_host
        self.supernode_port = supernode_port
        self.connect_with_node(supernode_host, supernode_port)
        self.supernode = self.all_nodes[0]

    def outbound_node_connected(self, connected_node):
        print("outbound_node_connected: " + connected_node.id)

    def inbound_node_connected(self, connected_node):
        print("inbound_node_connected: " + connected_node.id)

    def inbound_node_disconnected(self, connected_node):
        print("inbound_node_disconnected: " + connected_node.id)

    def outbound_node_disconnected(self, connected_node):
        print("outbound_node_disconnected: " + connected_node.id)

    def node_message(self, connected_node, data):
        print("node_message from " + connected_node.id + ": " + str(data))

        if data == 'information':
            if connected_node.host == self.supernode_host:
                information = subprocess.check_output(['ps', '-eo', '%cpu,pid', '--sort', '-%cpu'])
                self.send_to_node(self.supernode, information)
            else:
                print(data)
                self.send_to_node(self.supernode, "Hi, I'm Alive!")

    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")


