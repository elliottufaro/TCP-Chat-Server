import sys
import select
from socket import *

import builtins

# Redefine print for autograder -- do not modify
def print(*args, **kwargs):
    builtins.print(*args, **kwargs, flush=True)

bad_words = ["virus", "worm", "malware"]
good_words = ["groot", "hulk", "ironman"]

def replace_bad_words(s):
    for j in range(3):
        s = s.replace(bad_words[j], good_words[j])
    return s

if len(sys.argv) != 2:
    print("Usage: python3 " + sys.argv[0] + " port")
    sys.exit(1)
port = int(sys.argv[1])

print("server")


# Create a TCP socket to listen on port for new connections
tcp_server = socket(AF_INET, SOCK_STREAM)

# Bind the server's socket to port
tcp_server.bind(('0.0.0.0', port))

# Put listener_socket in LISTEN mode
tcp_server.listen()

# Accept a connection first from two clients
(comm_socket1, client_addr1) = tcp_server.accept()
(comm_socket2, client_addr2) = tcp_server.accept()

socket_list = [comm_socket1, comm_socket2]



# OR 
# implement accepting connections from multiple clients
# by including listener_socket in event handling 



active = True

while active:
    
    # Use select to see which socket is available to read from
    
    ready_sockets, _, _ = select.select(socket_list, [], [], 0)

    # recv on socket that is ready to read
    for notified_socket in ready_sockets:

        data = (notified_socket.recv(4096)).decode()

       

        if not data:
            active = False
        
        else:
        
            if notified_socket == comm_socket1:
                target_socket = comm_socket2
            else:
                target_socket = comm_socket1


            for i in range(len(bad_words)):
                if bad_words[i] in data:
                    data = data.replace(bad_words[i], good_words[i])
            
            target_socket.send(data.encode())
        print(data)


for socket in socket_list:
    socket.close()
socket_list.clear()

tcp_server.close()

            

                


    


    # Check to see if connection is closed


    # Filter and replace bad words

    # Forward to other sockets


# Close sockets