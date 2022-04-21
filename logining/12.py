import socket

def main(port):
    try:
        s = socket.socket()
        s.connect(("172.16.101.12",int(port)))
        print(port,"is open")
        s.close()
    except Exception as e:
        print(port,"is cloes")
        pass

if __name__ == '__main__':
    for port in range(1,65535):
        main(port)