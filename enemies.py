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

    def spawner(self, niveau):
        print(f"Ennemi '{self.type_ennemi}' apparu au niveau {niveau}")


# TODO: implémenter le boss final
# class BossFinale(Enemy):
#     def __init__(self):
#         super().__init__("Dragon Ancestral")
#         self.vie = 500
#         self.degats = 50
#         # on verra ça plus tard...