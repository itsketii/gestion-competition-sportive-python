class Equipe():
    def __init__(self, nom, drapeau, joueurs):
        self.nom = nom
        self.drapeau = drapeau
        self.joueurs = joueurs if joueurs is not None else []
        self.points = 0


    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)


    def ajouter_points(self, points):
        self.points += points