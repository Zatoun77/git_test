
from network import Network
n = Network()
x = input("T'envoie quoi ?")
for i in range(2):
    print("j'ai reçu :",(n.send(x)))

print("j'arrete la connexion")
print("j'ai reçu :",(n.send("stop")))