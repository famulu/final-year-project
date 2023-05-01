import sys, subprocess

from FileSharingNode import FileSharingNode



# The port to listen for incoming node connections
port = 9876 # default

supernode = {
    'ip': '34.125.89.16',
    'port': 9871
}

# Syntax file_sharing_node.py port
if len(sys.argv) > 1:
    port = int(sys.argv[1])

def message_callback(event, connected_node, data):
    if event == 'node_message' and connected_node.host == supernode['ip']:
        if data == 'information':
            information = subprocess.check_output(['ps','-eo', '%cpu,pid', '--sort', '-%cpu'])
            node.send_to_node(connected_supernode, information)
    else:
        print(data)
        node.send_to_node(connected_supernode, "Hi, I'm Alive!")

# Instantiate the node FileSharingNode, it creates a thread to handle all functionality
node = FileSharingNode("0.0.0.0", port)
node.on_node_message(message_callback)


# Start the node, if not started it shall not handle any requests!
node.start()

# The method prints the help commands text to the console
def print_help():
    print("stop - Stops the application.")
    print("help - Prints this help text.")

connected_supernode = None
def connect_to_node(node: FileSharingNode):
    host = input("host or ip of node? ")
    port = int(input("port? "))
    node.connect_with_node(host, port)
    for n in node.all_nodes:
        if n.host == supernode['ip'] and n.port == supernode['port']:
            global connected_supernode
            connected_supernode = n
            break

# Implement a console application
command = input("? ")
while command != "stop":
    if command == "help":
        print_help()
    if command == "connect":
        connect_to_node(node)

    command = input("? ")

node.stop()


