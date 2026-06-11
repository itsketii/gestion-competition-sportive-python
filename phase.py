from match import Match
import random


class Phase():
    def __init__(self, equipes):
        self.equipes = equipes
        self.groupes = {}
        self.matchs = []


    def  creer_groupe(self):
        for equipe in self.equipes:
            equipe.points = 0
        self.matchs = []
        random.shuffle(self.equipes)
        noms_groupes = ["Groupe A", "Groupe B", "Groupe C", "Groupe D"]
        for i in range(4):
            nom = noms_groupes[i]
            debut = i*4
            fin = debut+4
            self.groupes[nom] = self.equipes[debut:fin]


    def afficher_groupe(self):
        print("=== PHASE DE GROUPES ===")
        for nom_groupes, equipes in self.groupes.items():
            print(f"\n{nom_groupes} :")
            for equipe in equipes:
                print(f"  - {equipe.nom} ({equipe.points} pts)")

    def generer_match(self):
        for nom_groupe, equipes in self.groupes.items():
            for i in range(len(equipes)):
                for j in range(i+1, len(equipes)):
                    equipe1 = equipes[i]
                    equipe2 = equipes[j]
                    buts1 = random.randint(0, 5)
                    buts2 = random.randint(0, 5)
                    score = f"{buts1}-{buts2}"

                    if buts1 > buts2:
                        vainqueur = equipe1
                    elif buts2 > buts1:
                        vainqueur = equipe2
                    else:
                        vainqueur = None

                    match = Match(None, equipe1, equipe2, score, vainqueur)
                    self.matchs.append(match)

                    if vainqueur:
                        vainqueur.ajouter_points(3)
                    else:
                        equipe1.ajouter_points(1)
                        equipe2.ajouter_points(1)



    def determiner_qualifies(self):
        qualifies = []
        for nom_groupe, equipes in self.groupes.items():
            classement = sorted(equipes, key=lambda e: e.points, reverse=True)
            qualifies.extend(classement[:2])
            print(f"\n{nom_groupe} - Qualifiés :")
            print(f"  1er : {classement[0].nom} ({classement[0].points} pts)")
            print(f"  2ème : {classement[1].nom} ({classement[1].points} pts)")
        return qualifies