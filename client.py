import socket
import threading

# Define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 54321
ENCODER = 'utf-8'
BYTESIZE = 1024

# Get name
name = input("Enter a nickname: ")

# Create a client socket and connect to the server
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))


def receive_message():
    """Continuously receive messages from the server."""
    while True:
        try:
            message = client_socket.recv(BYTESIZE).decode(ENCODER)
            if message == 'name':
                client_socket.send(name.encode(ENCODER))
            else:
                print(message)
        except:
            print("An error occurred. Disconnecting...")
            client_socket.close()
            break


def send_message():
    """Continuously send messages to the server."""
    while True:
        message = input("")
        if message.lower() == "exit":  # Check if the user wants to exit
            client_socket.send(f"{name} has left the chat.".encode(ENCODER))
            client_socket.close()
            print("You have disconnected from the chat.")
            break
        else:
            client_socket.send(f"{name}: {message}".encode(ENCODER))


# Start threads for sending and receiving messages
receive_thread = threading.Thread(target=receive_message)
receive_thread.start()

send_thread = threading.Thread(target=send_message)
send_thread.start()
