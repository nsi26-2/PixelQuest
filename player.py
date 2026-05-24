# Gestion du personnage joueur
# Auteur : nsi26-1

class Player:
    VIE_MAX = 100

    def __init__(self, nom):
        self.nom = nom
        self.vie = Player.VIE_MAX
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

    def soigner(self, points_soin):
        self.vie = min(self.vie + points_soin, Player.VIE_MAX)
        print(f"Soin de {points_soin} PV. Vie actuelle : {self.vie}/{Player.VIE_MAX}")

    def afficher_stats(self):
        print(f"Joueur : {self.nom}")
        print(f"Vie : {self.vie}/{Player.VIE_MAX}")
        print(f"Score : {self.score}")
        print(f"Niveau : {self.niveau}")
        print(f"Position : ({self.position_x}, {self.position_y})")

    def est_en_collision(self, ennemi):
        # fix: la détection de collision était inversée
        distance_x = abs(self.position_x - ennemi.position_x)
        distance_y = abs(self.position_y - ennemi.position_y)
        return distance_x < 32 and distance_y < 32