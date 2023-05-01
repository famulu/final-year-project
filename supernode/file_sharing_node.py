import sys

from FileSharingNode import FileSharingNode

# The port to listen for incoming node connections
port = 9871 # default

# Syntax file_sharing_node.py port
if len(sys.argv) > 1:
    port = int(sys.argv[1])

# Instantiate the node FileSharingNode, it creates a thread to handle all functionality
node = FileSharingNode("0.0.0.0", port)

# Start the node, if not started it shall not handle any requests!
node.start()

# The method prints the help commands text to the console
def print_help():
    print("stop - Stops the application.")
    print("help - Prints this help text.")
    print("connect - Connect to a node")
    print("broadcast - Send message to all connected nodes")
    print("status - Displays the number of connected nodes and their details")


def connect_to_node(node: FileSharingNode):
    host = input("host or ip of node? ")
    port = int(input("port? "))
    node.connect_with_node(host, port)

def broadcast(node: FileSharingNode):
    node.send_to_nodes('Hello, World')


# Implement a console application
command = input("? ")
print_help()
while command != "stop":
    if command == "help":
        print_help()
    elif command == "connect":
        connect_to_node(node)
    elif command == "broadcast":
        broadcast(node)
    elif command == "status":
        node.print_connections()
        for n in node.all_nodes:
            print(n.host + ':' + n.port)

    command = input("? ")

node.stop()


