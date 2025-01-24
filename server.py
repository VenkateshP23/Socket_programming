import socket
import threading

# Define constants
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 54321
ENCODER = 'utf-8'
BYTESIZE = 1024

# Create server socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST_IP, HOST_PORT))
server_socket.listen()

# Lists to store connected clients and their names
client_socket_list = []
client_name_list = []
is_running = True  # Flag to control the server loop


def broadcast_message(message):
    """Send a message to all connected clients."""
    for client in client_socket_list:
        try:
            client.send(message)
        except:
            continue


def receive_message(client_socket):
    """Receive and broadcast messages from a client."""
    while True:
        try:
            message = client_socket.recv(BYTESIZE)
            broadcast_message(message)
        except:
            # Handle client disconnection
            index = client_socket_list.index(client_socket)
            client_socket_list.remove(client_socket)
            client_socket.close()

            name = client_name_list[index]
            broadcast_message(f"{name} has left the chat.".encode(ENCODER))
            client_name_list.remove(name)
            break


def connect_client():
    """Accept and handle new client connections."""
    while is_running:
        try:
            client_socket, client_address = server_socket.accept()
            print(f"Connected with {str(client_address)}")

            # Get the name of the client
            client_socket.send('name'.encode(ENCODER))
            name = client_socket.recv(BYTESIZE).decode(ENCODER)

            # Add the client to the lists
            client_name_list.append(name)
            client_socket_list.append(client_socket)

            print(f"Name of the client is {name}")
            broadcast_message(f"{name} joined the chat!".encode(ENCODER))
            client_socket.send("You are connected to the server!".encode(ENCODER))

            # Start a thread to receive messages from the client
            thread = threading.Thread(target=receive_message, args=(client_socket,))
            thread.start()
        except:
            break


def server_exit():
    """Shut down the server gracefully."""
    global is_running
    is_running = False
    print("Server is shutting down...")

    # Notify all clients about the shutdown
    broadcast_message("Server is shutting down. You have been disconnected.".encode(ENCODER))

    # Close all client connections
    for client in client_socket_list:
        try:
            client.close()
        except:
            continue

    # Close the server socket
    server_socket.close()
    print("Server shut down successfully.")


# Main server logic
print("Server is listening...")
server_thread = threading.Thread(target=connect_client)
server_thread.start()

try:
    while is_running:
        pass  # Keep the server running until a manual stop or exception occurs
except KeyboardInterrupt:
    server_exit()
