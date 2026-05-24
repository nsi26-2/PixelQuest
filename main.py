# PixelQuest - Point d'entrée du jeu
# Auteur : ME :)
# Modifié par : nsi26-2

import sys
from player import Player
from enemies import Enemy

def initialiser():
    if sys.platform == "win32":
        print("Système Windows détecté - ajustement des paramètres...")
    print("Initialisation OK")

def charger_niveau(numero):
    print(f"Chargement du niveau {numero}...")
    ennemis = []
    for i in range(numero * 2):
        e = Enemy("Goblin")
        e.spawner(numero)
        ennemis.append(e)
    return ennemis

def boucle_jeu(joueur, ennemis):
    print(f"\n=== Niveau en cours ===")
    print(f"DEBUG: {len(ennemis)} ennemis chargés")
    for ennemi in ennemis:
        ennemi.attaquer(joueur)
    joueur.afficher_stats()

def main():
    print("Lancement de PixelQuest...")
    initialiser()
    joueur = Player("Hero")
    ennemis = charger_niveau(1)
    boucle_jeu(joueur, ennemis)

if __name__ == "__main__":
    main()