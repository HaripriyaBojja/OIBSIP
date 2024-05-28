import socket
import threading

class Server:
    def __init__(self, port):
        self.port = port
        self.clients = []
        self.server_socket = None

    def start(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(('0.0.0.0', self.port))
        self.server_socket.listen(5)
        print("Server started. Waiting for connections...")
        self.accept_clients()  

    def accept_clients(self):
        while True:
            client_socket, addr = self.server_socket.accept()
            self.clients.append(client_socket)
            print(f"Connection from {addr}")
            threading.Thread(target=self.handle_client, args=(client_socket,)).start()

    def handle_client(self, client_socket):
        while True:
            try:
                message = client_socket.recv(1024).decode('utf-8')
                if message:
                    self.broadcast(message, client_socket)
                else:
                    self.remove_client(client_socket)
                    break
            except:
                self.remove_client(client_socket)
                break

    def broadcast(self, message, sender_socket):
        for client_socket in self.clients:
            if client_socket != sender_socket:
                try:
                    client_socket.send(message.encode('utf-8'))
                except:
                    self.remove_client(client_socket)

    def remove_client(self, client_socket):
        if client_socket in self.clients:
            self.clients.remove(client_socket)
            client_socket.close()

def main():
    server = Server(5555)
    server.start()

if __name__ == "__main__":
    main()
