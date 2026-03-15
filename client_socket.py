import socket

HOST = "127.0.0.1"
PORT = 8080


def client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect((HOST, PORT))

    print("✅ Serverga ulandik!")


    message = client_socket.recv(1024).decode()
    print("Server:", message.strip())


    while True:
        text = input("Siz: ")
        client_socket.sendall((text + "\n").encode())

        reply = client_socket.recv(1024).decode()
        print("Server:", reply.strip())


if __name__ == '__main__':
    client()
