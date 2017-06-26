import socket
from threading import Thread

HOST = "192.168.1.9"
PORT = 25565

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

s.listen(100)

print "Started server"

class Client:
    def __init__(self, conn, addr):
        self.conn = conn
        self.addr = addr

    def send(self, data):
        self.conn.send(data)

clients = []


def listen_for_clients():
    global clients
    while True:
        conn, addr = s.accept()
        clients.append(Client(conn, addr))
        print "Client connected at " + addr[0] + ":" + str(addr[1]) + "\n"

def main():
    global clients
    while len(clients) == 0: pass
    while True:
        ui = raw_input("Server: ")
        try:
            for i in clients:
                try: i.send(ui)
                except: pass
        except: print "failed to send"
    

if __name__ == "__main__":
    t1 = Thread(target=listen_for_clients, args=())
    t2 = Thread(target=main, args=())
    t1.start()
    t2.start()
    
