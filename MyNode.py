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
            if connected_node.host == self.supernode_host and connected_node.port == self.supernode_port:
                info = subprocess.check_output(['ps', '-eo', '%cpu,%mem,pid', '--sort', '-%cpu']).decode('utf-8').splitlines()
                cleaned_info = []
                cleaned_info.append(info[0])
                for i in range(1, len(info)):
                    row = info[i]
                    if row.split()[0] != '0.0' or row.split()[1] != '0.0':
                        cleaned_info.append(row)
                cleaned_info = "\n".join(cleaned_info)
                print("***")
                print(cleaned_info)
                print("***")
                info = '\n'.join(info)
                self.send_to_node(self.supernode, "\n" + cleaned_info)
            else:
                print(data)
                self.send_to_node(connected_node, "Hi, I'm Alive!")

    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")


