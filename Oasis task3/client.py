import socket
import threading

PORT = 5051
HEADER = 64
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


def send(msg):
    try:
        message = msg.encode(FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(FORMAT)
        send_length += b' ' * (HEADER - len(send_length))
        client.send(send_length)
        client.send(message)
    except (ConnectionResetError, BrokenPipeError) as e:
        print(f"Connection error: {e}. Unable to send message.")
        client.close()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        client.close()


def receive():
    while True:
        try:
            message_length = client.recv(HEADER).decode(FORMAT)
            if message_length:
                message_length = int(message_length.strip())
                message = client.recv(message_length).decode(FORMAT)
                print(f"Server: {message}")
        except (ConnectionResetError, BrokenPipeError) as e:
            print(f"Connection error: {e}. Unable to receive message.")
            client.close()
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            client.close()
            break


receive_thread = threading.Thread(target=receive)
receive_thread.start()

try:
    print("Type your messages below:")
    while True:
        msg = input()
        send(msg)
        if msg == DISCONNECT_MESSAGE:
            break
except KeyboardInterrupt:
    print("\n[DISCONNECTED] Keyboard interrupt received, disconnecting...")
    send(DISCONNECT_MESSAGE)
finally:
    client.close()
