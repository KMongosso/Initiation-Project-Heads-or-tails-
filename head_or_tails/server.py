#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import select


def displayPlayers(playersDict):
    print("\n\n*******************   TABLEAU DES SCORES   *******************\n\n");
    for player in playersDict.values():
        print(player[0] +"\t:\t"+player[1]+"\n")

    print("\n\n")
    

hote = ''
port = 12800

playersDict = {}

connexion_principale = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connexion_principale.bind((hote, port))
connexion_principale.listen(5)
print("Le serveur écoute à présent sur le port {}".format(port))

serveur_lance = True
clients_connectes = []
while serveur_lance:
    # On va vérifier que de nouveaux clients ne demandent pas à se connecter
    # Pour cela, on écoute la connexion_principale en lecture
    # On attend maximum 50ms
    connexions_demandees, wlist, xlist = select.select([connexion_principale],
        [], [], 0.05)
    
    for connexion in connexions_demandees:
        connexion_avec_client, infos_connexion = connexion.accept()
        # On ajoute le socket connecté à la liste des clients
        clients_connectes.append(connexion_avec_client)
    
    # Maintenant, on écoute la liste des clients connectés
    # Les clients renvoyés par select sont ceux devant être lus (recv)
    # On attend là encore 50ms maximum
    # On enferme l'appel à select.select dans un bloc try
    # En effet, si la liste de clients connectés est vide, une exception
    # Peut être levée
    clients_a_lire = []
    try:
        clients_a_lire, wlist, xlist = select.select(clients_connectes,
                [], [], 0.05)
    except select.error:
        pass
    else:
        # On parcourt la liste des clients à lire
        for client in clients_a_lire:
            # Client est de type socket
            msg_recu = client.recv(1024)
            # Peut planter si le message contient des caractères spéciaux
            msg_recu = msg_recu.decode()
            if msg_recu[0] == 'C':
                playersDict[client] = [msg_recu[2:],'0']
                print(playersDict[client][0])
            elif msg_recu[0] == 'S':
                playersDict[client][1] = msg_recu[2:]
                displayPlayers(playersDict)
            elif msg_recu == "fin":
                clients_a_lire.remove(client)
                clients_connectes.remove(client)

print("Fermeture des connexions")
for client in clients_connectes:
    client.close()

connexion_principale.close()
