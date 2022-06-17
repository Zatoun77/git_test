from network import Network
import time
n = Network()
x = input("T'envoie quoi ?")
for i in range(2):
    print("j'ai reçu :",(n.send(x)))
    time.sleep(2)

print("j'arrete la connexion")
print("j'ai reçu :",(n.send("stop")))