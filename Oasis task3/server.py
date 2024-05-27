import socket
import threading

PORT = 5051
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(ADDR)

clients = []


def broadcast(message, _client):
    for client in clients:
        if client != _client:
            try:
                client.send(message)
            except (ConnectionResetError, BrokenPipeError) as e:
                print(f"Connection error: {e}. Closing connection.")
                client.close()
                clients.remove(client)
            except Exception as e:
                print(f"Unexpected error during broadcast: {e}")
                client.close()
                clients.remove(client)


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    connected = True
    while connected:
        try:
            msg_length = conn.recv(HEADER).decode(FORMAT)
            if msg_length:
                msg_length = int(msg_length.strip())
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}] {msg}")
                broadcast(msg.encode(FORMAT), conn)
        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"Connection lost with {addr}: {e}")
            connected = False
        except Exception as e:
            print(f"An unexpected error occurred with {addr}: {e}")
            connected = False
    conn.close()
    if conn in clients:
        clients.remove(conn)


def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        try:
            conn, addr = server.accept()
            clients.append(conn)
            thread = threading.Thread(target=handle_client, args=(conn, addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")


print("[STARTING] Server is starting...")
start()
