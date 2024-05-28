import socket
import threading

class Client:
    def __init__(self, server_address, port):
        self.server_address = server_address
        self.port = port
        self.client_socket = None

    def start(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.server_address, self.port))
        threading.Thread(target=self.receive_messages).start()
        self.send_messages()

    def receive_messages(self):
        while True:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(message)
            except:
                print("An error occurred!")
                self.client_socket.close()
                break

    def send_messages(self):
        while True:
            message = input("")
            if message:
                self.client_socket.send(message.encode('utf-8'))

def main():
    server_address = input("Enter server IP address: ")
    client = Client(server_address, 5555)
    client.start()

if __name__ == "__main__":
    main()
