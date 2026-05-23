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
        # Inflige des dégâts au joueur
        joueur.vie = joueur.vie - self.degats
        print(f"{self.type_ennemi} attaque ! -{self.degats} PV")

    def spawner(niveau):
        # Fait apparaître un ennemi selon le niveau
        print(f"Ennemi apparu au niveau {niveau}")