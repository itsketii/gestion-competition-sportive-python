class Competition():
    def __init__(self, nom, description, date_debut, date_fin):
        self.nom = nom
        self.description = description
        self.date_debut = date_debut
        self.date_fin = date_fin
        self.equipes = []
        self.matchs = []
        self.joueurs = []
        self.postes = []


    def ajouter_poste(self, poste):
        self.postes.append(poste)
        print(f"Poste ajouté : {poste.nom} - {poste.description}")

    def ajouter_joueur(self, joueur):
        self.joueurs.append(joueur)
        poste_nom = joueur.poste.nom if joueur.poste is not None else "Sans poste"
        print(f"Joueur ajouté : {joueur.nom} - {poste_nom}")

    def ajouter_equipe(self, equipe):
        self.equipes.append(equipe)
        print(f"Equipe ajoutée : {equipe.nom} - {equipe.drapeau}")

    def ajouter_match(self, match):
        self.matchs.append(match)
        print(f"Match ajouté : {match.equipe1.nom} vs {match.equipe2.nom} - {match.date}")

    def afficher_postes(self):
        print("Postes :")
        for poste in self.postes:
            print(f"{poste.nom} - {poste.description}")    

    def afficher_joueurs(self):
        print("Joueurs :")
        for joueur in self.joueurs:
            poste_nom = joueur.poste.nom if joueur.poste is not None else "Sans poste"
            equipe_nom = joueur.equipe.nom if getattr(joueur, "equipe", None) is not None else "Sans equipe"
            print(f"{joueur.nom} - {poste_nom} - {equipe_nom}")

    def afficher_equipes(self):
        print("Equipes :")
        for equipe in self.equipes:
            print(f"{equipe.nom} - {equipe.drapeau}")
    
    def afficher_matchs(self):
        print("Matchs :")
        for match in self.matchs:
            print(f"{match.equipe1.nom} vs {match.equipe2.nom} - {match.date}")

    def supprimer_poste(self, poste):
        self.postes.remove(poste)

    def supprimer_joueur(self, joueur):
        self.joueurs.remove(joueur)

    def supprimer_equipe(self, equipe):
        self.equipes.remove(equipe)

    def supprimer_match(self, match):
        self.matchs.remove(match)