import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.1.2"
        self.port = 1111
        self.addr = (self.server, self.port)
        self.connect()

    def connect(self):
        try:
            print("Connection au server...")
            self.client.connect(self.addr)
            print("Connexion réussie")
        except:
            print("Connexion echouer")
        print("")
            

    def send(self, data):
        try:
            print("--------------------------")
            self.client.sendall(str.encode(data))
            print("C'est envoyer")
            return self.client.recv(2048).decode()
        except socket.error as e:
            print("Problème lors de l'envoie :",e)
        

