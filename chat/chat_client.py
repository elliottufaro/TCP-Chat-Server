import sys
import signal
import sys
import select
from socket import *
import builtins

'cd Networks_Homework/Networks_HW/assignment1/chat'


if len(sys.argv) != 3:
    print("Usage: python3 " + sys.argv[0] + "server_address server_port")
    sys.exit(1)

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

server_address = sys.argv[1]
relay_port = int(sys.argv[2])

print("client")

# Create a socket for the sender
tcp_client = socket(AF_INET, SOCK_STREAM)


# Connect sender to the server at the server_port
tcp_client.connect((server_address, relay_port))


# Set up a list of file descriptors to read from
stdin = sys.stdin.fileno()
fileno = tcp_client.fileno()
all_fds = [stdin, fileno] # Add your sockets fileno() here
#all_fds.append(tcp_client.fileno())



# Repeat until server goes down or user stops entering in data
try:
    while True:
        ready_fds, _, _ = select.select(all_fds, [],[], 5)
        
        # Send data if you stdin is in ready_fds (i.e. if user pressed enter)
        if stdin in ready_fds:
            tcp_client.send(input().encode())

        if fileno in ready_fds:
            data = (tcp_client.recv(4096)).decode()
            if not data:
                break
            else:
                print(data)


        # Receive data if socket fileno is in ready_fds


    # Close the socket
    tcp_client.close()


except KeyboardInterrupt:

    tcp_client.close()


