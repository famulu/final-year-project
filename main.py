from MyNode import MyNode
from Supernode import Supernode



# The port to listen for incoming node connections
port = 9876 # default


# supernode = {
#     'ip': '34.125.89.16',
#     'port': 9871
# }

# Syntax main.py port
# if len(sys.argv) > 1:
#     port = int(sys.argv[1])

# Instantiate the node, it creates a thread to handle all functionality
print("Choose the type of node:")
print("1. Node")
print("2. Supernode")
result = input("> ")
while result.lower() not in ["1", "2", "node", "supernode"]:
    print("Invalid input.")
    result = input("> ")

if result in ["1", "node"]:
    supernode_host = input("Host or IP of supernode: ")
    supernode_port = int(input("Port: "))
    node = MyNode("0.0.0.0", port, supernode_host, supernode_port)

    # Start the node, if not started it shall not handle any requests!
    node.start()


    # The method prints the help commands text to the console
    def print_help():
        print("stop - Stops the application.")
        print("help - Prints this help text.")


    def connect_to_node(node: MyNode):
        host = input("Host or ip of node: ")
        port = int(input("Port: "))
        node.connect_with_node(host, port)


    # Implement a console application
    print_help()
    command = input("> ")
    while command != "stop":
        if command == "help":
            print_help()
        if command == "connect":
            connect_to_node(node)

        command = input("> ")

    node.stop()

else:
    # The port to listen for incoming node connections
    port = 9871  # default

    # Instantiate the node FileSharingNode, it creates a thread to handle all functionality
    node = Supernode("0.0.0.0", port)

    # Start the node, if not started it shall not handle any requests!
    node.start()


    # The method prints the help commands text to the console
    def print_help():
        print()
        print("stop - Stops the application.")
        print("help - Prints this help text.")
        print("connect - Connect to a node")
        print("broadcast - Send message to all connected nodes")
        print("status - Displays the number of connected nodes and their details")


    def connect_to_node(node: Supernode):
        host = input("host or ip of node? ")
        port = int(input("port? "))
        node.connect_with_node(host, port)


    # Implement a console application
    print_help()
    command = input("> ")
    while command != "stop":
        if command == "help":
            print_help()
        elif command == "connect":
            connect_to_node(node)
        elif command == "broadcast":
            node.broadcast()
        elif command == "status":
            node.connected_nodes_status()

        command = input("> ")

    node.stop()



