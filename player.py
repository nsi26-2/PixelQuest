# Gestion du personnage joueur
# Auteur : nsi26-1

class Player:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.position_x = 0
        self.position_y = 0
        self.score = 0

    def afficher_stats(self):
        print(f"Joueur : {self.nom}")
        print(f"Vie : {self.vie}")
        print(f"Position : ({self.position_x}, {self.position_y})")
        print(f"Score : {self.score}")