from p2pnetwork.node import Node


class Supernode(Node):
    is_supernode = True

    def __init__(self, host, port, id=None, callback=None, max_connections=0):
        super(Supernode, self).__init__(host, port, id, callback, max_connections)

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

    def node_disconnect_with_outbound_node(self, connected_node):
        print("node wants to disconnect with oher outbound node: " + connected_node.id)

    def node_request_to_stop(self):
        print("node is requested to stop!")

    # Get performance information from all connected nodes
    def broadcast(self):
        self.send_to_nodes('information')

    def connected_nodes_status(self):
        self.print_connections()
        print()
        if len(self.all_nodes):
            print("Nodes:")
            for n in self.all_nodes:
                print('- ' + n.host + ':' + n.port)
