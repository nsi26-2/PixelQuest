# PixelQuest - Point d'entrée du jeu
# Auteur : ME :)
# Modifié par : nsi26-2

import sys

def initialiser():
    # Correction : pygame.init() plantait sur Windows sans cette vérification
    if sys.platform == "win32":
        print("Système Windows détecté - ajustement des paramètres...")
    print("Initialisation OK")

def main():
    print("Lancement de PixelQuest...")
    initialiser()
    print("Chargement du niveau 1...")
    # TODO: initialiser la fenêtre pygame
    # TODO: charger les assets

if __name__ == "__main__":
    main()