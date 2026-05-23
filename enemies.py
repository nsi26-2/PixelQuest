# Gestion des ennemis
# Auteur : nsi26-2

class Enemy:
    def __init__(self, type_ennemi):
        self.type_ennemi = type_ennemi
        self.vie = 30
        self.degats = 10
        self.position_x = 100
        self.position_y = 100

    def attaquer(self, joueur):
        joueur.vie = joueur.vie - self.degats
        print(f"{self.type_ennemi} attaque ! -{self.degats} PV")

    # Correction bug-slayer99 : manquait le "self" en paramètre, 
    # les ennemis ne spawnaient plus à partir du niveau 3
    def spawner(self, niveau):
        print(f"Ennemi '{self.type_ennemi}' apparu au niveau {niveau}")