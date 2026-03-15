import socket
from http.client import responses
import threading

HOST = "127.0.0.1"
PORT = 8080


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind((HOST, PORT))
    sock.listen()
    print(f"Server {HOST}:{PORT} da ishga tushdi! Client kutyapdi")
    while True:
        client_socket, addr = sock.accept()
        thread = threading.Thread(
            target=connection,
            args=(client_socket, addr),
            daemon=True
        )
        thread.start()


def connection(conn, addr):
    try:
        conn.sendall(b"Salom! TCP serverga ulanding Xush kelibsan.\n")


        while True:
            data = conn.recv(1024)

            if not data:
                break
            text = data.decode().strip()
            print(f"Mijoz ({addr}) yozdi: {text}")

            response = f"Server: {text}\n"
    except Exception as e:
        print(("Xato" , e))
    finally:
        conn.close()
        print(f"Mijoz uzuldi")
if __name__ == '__main__':
    main()
