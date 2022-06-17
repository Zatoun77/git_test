import socket
import threading

class ClientThread(threading.Thread):

    def __init__(self, ip, port, clientsocket):

        threading.Thread.__init__(self)
        self.ip = ip
        self.port = port
        self.clientsocket = clientsocket
        print("[+] Nouveau thread pour %s %s" % (self.ip, self.port, ))

    def run(self): 
   
        print("Connexion de %s %s" % (self.ip, self.port, ))
        while True:
            try:
                data = self.clientsocket.recv(2048).decode()
                if data == "stop":
                    reply = "Fin de la connection"
                    self.clientsocket.send(reply.encode())
                    break
                
                reply = "Bien recu"

                print('recue :',data)
                print('envoyer :',reply)
                self.clientsocket.send(reply.encode())
            except:
                print("Connection coupé")
                break

        print("Client déconnecté...")


HOST = "192.168.1.2"
PORT = 1111

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcpsock.bind(("",PORT))

while True:
    tcpsock.listen()
    (clientsocket, (HOST, PORT)) = tcpsock.accept()
    newthread = ClientThread(HOST, PORT, clientsocket)
    newthread.start()