This project is a TCP message server/relay application that facilitates communication between two clients through a proxy server. The server filters and replaces specified bad words in the messages with good words before relaying the messages to the other client. This project includes both server and client implementations in Python.

Server Implementation
The server listens for incoming TCP connections from clients, accepts two connections, and then relays messages between the two clients. Before relaying, the server replaces any bad words found in the messages with specified good words. The server utilizes the select module to handle multiple connections efficiently.

Features:
Accepts connections from two clients.
Filters and replaces bad words in the messages.
Relays messages between the two clients.
Closes connections gracefully.

Run the server script with a specified port number:
python3 server.py <port>



Client Implementation
The client connects to the server and allows the user to send messages. It also receives and displays messages from the other client, filtered through the server.

Features:
Connects to the server.
Sends user input to the server.
Receives and displays messages from the server.
Closes the connection gracefully on exit.


Run the client script with the server address and port number:
python3 client.py <server_address> <server_port>
