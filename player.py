# Gestion du personnage joueur
# Auteur : nsi26-1

class Player:
    def __init__(self, nom):
        self.nom = nom
        self.vie = 100
        self.position_x = 0
        self.position_y = 0
        self.score = 0
        self.niveau = 1

    def gagner_points(self, points):
        self.score += points
        print(f"+{points} points ! Score total : {self.score}")

    def monter_niveau(self):
        self.niveau += 1
        print(f"Niveau {self.niveau} atteint !")

    def afficher_stats(self):
        print(f"Joueur : {self.nom}")
        print(f"Vie : {self.vie}")
        print(f"Score : {self.score}")
        print(f"Niveau : {self.niveau}")
        print(f"Position : ({self.position_x}, {self.position_y})")