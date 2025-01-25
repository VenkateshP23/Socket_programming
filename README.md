# Multi-Client Chat Room

This is a simple client-server chat application written in Python. It allows multiple clients to connect to a single server, send messages to each other in real time, and gracefully handle client and server disconnections.

---

## Features

- **Real-Time Communication**: Clients can send and receive messages in real time.
- **Multi-Client Support**: The server handles multiple clients simultaneously using threading.
- **Graceful Disconnection**: Clients and the server handle disconnections (manual or unexpected) without crashing.
- **Server Shutdown Notification**: The server can broadcast a message to all clients before shutting down.
- **Exit Option for Clients**: Clients can type `exit` to leave the chat room.

---

## Requirements

- Python 3.x
- A terminal or command-line interface

---

## How It Works

1. The **server** listens for incoming connections and handles multiple clients using threads.
2. Clients can connect to the server and join the chat room by providing a nickname.
3. Messages sent by any client are broadcasted to all connected clients by the server.
4. Both clients and the server handle clean disconnections:
   - Clients typing `exit` will disconnect from the server.
   - If the server shuts down, all clients are notified and disconnected.

---

## Setup and Usage

### Clone the Repository
```bash
git clone https://github.com/VenkateshP23/Socket_programming.git
cd Socket_programming
```

### Run the Server
Open a terminal.
Navigate to the project directory.
Run the server script:
```bash
python server.py
```
The server will start listening for connections.

### Run the client
Open another terminal (or multiple terminals for multiple clients).
Navigate to the project directory.
Run the client script:
```bash
python client.py
```
Enter a nickname when prompted to join the chat.

### Exit the Chat
Clients can type **exit** to disconnect from the chat room.
The server admin can shut down the server, notifying all connected clients.

---

Here’s a screenshot of the application in action:
![Chat Application Output](images/Screenshot%20(385).png)

