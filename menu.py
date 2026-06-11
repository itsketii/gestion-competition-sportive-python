from poste import Poste
from phase import Phase
from joueur import Joueur
from equipe import Equipe
from match import Match
from DB_app_console_CAN_Ketsia import sauvegarder_competition


def _trouver_poste(competition, nom_poste):
    nom_normalise = nom_poste.strip().lower()
    for poste in competition.postes:
        if poste.nom.strip().lower() == nom_normalise:
            return poste
    return None


def _trouver_equipe(competition, nom_equipe):
    nom_normalise = nom_equipe.strip().lower()
    for equipe in competition.equipes:
        if equipe.nom.strip().lower() == nom_normalise:
            return equipe
    return None




def menu_demarage(competition):
    print("AKWAKA")
    while True:
        print("Menu:")
        choix = input("1.Ajouter un poste"
                  "\n2.Ajouter un joueur"
                  "\n3.Ajouter une equipe"
                  "\n4.Ajouter un match"
                  "\n5.Afficher les postes"
                  "\n6.Afficher les joueurs"
                  "\n7.Afficher les equipes"
                  "\n8.Afficher un match"
                  "\n9.Sauvegarder les données"
                  "\n10.Supprimer un joueur"
                  "\n11.Supprimer un poste"
                  "\n12.Supprimer une equipe"
                  "\n13.Supprimer un match"
                  "\n14.Lancer la compétition"
                  "\n15.Quitter"
                  "\nChoisissez une option: ")
        print()



        if choix == "1":
            print("1.Ajouter un poste")
            # Code pour ajouter un poste
            nom = input("Nom du poste: ")
            description = input("Description du poste: ")
            nouveau_poste = Poste(nom, description)
            competition.ajouter_poste(nouveau_poste)

        elif choix == "2":
            print("2.Ajouter un joueur")
            # Code pour ajouter un joueur
            if len(competition.postes) == 0:
                print("Ajoute d'abord au moins un poste.")
                continue
            nom = input("Nom du joueur: ")
            prenoms = input("Prenoms du joueur: ")
            nationalite = input("Nationalité du joueur: ")
            taille = input("Taille du joueur: ")
            poids = input("Poids du joueur: ")
            pied_fort = input("Pied fort du joueur: ")
            competition.afficher_postes()
            nom_poste = input("Poste du joueur (saisir le nom exact): ")
            poste_du_joeur = _trouver_poste(competition, nom_poste)
            if poste_du_joeur is None:
                print("Poste introuvable. Joueur non ajouté.")
                continue
            competition.afficher_equipes()
            nom_equipe = input("Equipe du joueur (laisser vide si aucune): ")
            equipe_du_joueur = None if nom_equipe.strip() == "" else _trouver_equipe(competition, nom_equipe)
            if nom_equipe.strip() != "" and equipe_du_joueur is None:
                print("Equipe introuvable. Joueur non ajouté.")
                continue

            nouveau_joueur = Joueur(nom, prenoms, nationalite, taille, poids, pied_fort, poste_du_joeur, equipe_du_joueur)
            competition.ajouter_joueur(nouveau_joueur)
            if equipe_du_joueur is not None:
                equipe_du_joueur.ajouter_joueur(nouveau_joueur)

        elif choix == "3":
            print("3.Ajouter une equipe")
            # Code pour ajouter une equipe
            nom = input("Nom de l'équipe: ")
            drapeau = input("Drapeau de l'équipe: ")
            nouvelle_equipe = Equipe(nom, drapeau, [])
            competition.ajouter_equipe(nouvelle_equipe)

        elif choix == "4":
            print("4.Ajouter un match")
            # Code pour Ajouter un match
            if len(competition.equipes) < 2:
                print("Il faut au moins 2 equipes pour creer un match.")
                continue
            date = input("Date du match: ")
            equipe_1 = _trouver_equipe(competition, input("Nom de l'équipe 1: "))
            equipe_2 = _trouver_equipe(competition, input("Nom de l'équipe 2: "))
            if equipe_1 is None or equipe_2 is None:
                print("Equipe introuvable. Match non ajouté.")
                continue
            if equipe_1 == equipe_2:
                print("Un match doit opposer 2 equipes differentes.")
                continue
            score = input("Score du match: ")
            vainqueur_saisi = input("Vainqueur du match (laisser vide pour nul): ")
            vainqueur = None if vainqueur_saisi.strip() == "" else _trouver_equipe(competition, vainqueur_saisi)
            if vainqueur is not None and vainqueur not in (equipe_1, equipe_2):
                print("Le vainqueur doit etre l'equipe 1, l'equipe 2 ou vide pour un nul.")
                continue
            nouveau_match = Match(date, equipe_1, equipe_2, score, vainqueur)
            competition.ajouter_match(nouveau_match)

        elif choix == "5":
            print("5.Afficher les postes")
            # Code pour afficher les postes
            competition.afficher_postes()

        elif choix == "6":
            print("6.Afficher les joueurs")
            # Code pour afficher les joueurs
            competition.afficher_joueurs()

        elif choix == "7":
            print("7.Afficher les equipes")
            # Code pour afficher les equipes
            competition.afficher_equipes()
            nom = input("Entrez le nom d'une équipe pour voir ses joueurs (ou Entrée pour passer) : ")
            if nom:
                for equipe in competition.equipes:
                    if equipe.nom == nom:
                        print(f"\nJoueurs de {equipe.nom} :")
                        for joueur in equipe.joueurs:
                            poste_nom = joueur.poste.nom if joueur.poste is not None else "Sans poste"
                            print(f"  {joueur.nom} {joueur.prenoms} - {poste_nom}")

        elif choix == "8":
            print("8.Afficher les matchs")
            # Code pour afficher les matchs
            competition.afficher_matchs()

        elif choix == "9":
            print("9.Sauvegarder les données")
            # Code pour sauvegarder les données
            sauvegarder_competition(competition)

        elif choix == "10":
            print("10.Supprimer un poste")
            # Code pour supprimer un joueur
            competition.afficher_joueurs()
            nom = input("Nom du joueur à supprimer: ")
            for j in competition.joueurs:
                if j.nom == nom:
                    competition.supprimer_joueur(j)
                    print(f"Joueur {nom} supprimé.")
                    break

        elif choix == "11":
            print("11.Supprimer un poste")
            # Code pour supprimer un poste
            competition.afficher_postes()
            nom = input("Nom du poste à supprimer: ")
            for p in competition.postes:
                if p.nom == nom:
                    competition.supprimer_poste(p)
                    print(f"Poste {nom} supprimé.")
                    break

        elif choix == "12":
            print("12.Supprimer une equipe")
            # Code pour supprimer une equipe
            competition.afficher_equipes()
            nom = input("Nom de l'équipe à supprimer: ")
            for e in competition.equipes:
                if e.nom == nom:
                    competition.supprimer_equipe(e)
                    print(f"Equipe {nom} supprimé.")
                    break

        elif choix == "13":
            print("13.Supprimer un match")
            # Coce pour supprimer un match
            competition.afficher_matchs()
            eq1 = input("Equipe 1 du match à supprimer: ")
            eq2 = input("Equipe 2 du match à supprimer: ")
            for m in competition.matchs:
                if m.equipe1.nom == eq1 and m.equipe2.nom == eq2:
                    competition.supprimer_match(m)
                    print(f"Match {eq1} vs {eq2} supprimé.")
                    break


        elif choix == "14":
            print("14. Lancer la compétition")
            if len(competition.equipes) < 16:
                print(f"Il faut 16 équipes ! ({len(competition.equipes)} équipes enregistrées)")
            else:
                phase = Phase(competition.equipes)
                phase.creer_groupe()
                phase.afficher_groupe()
                phase.generer_match()
                phase.determiner_qualifies()
                competition.matchs = list(phase.matchs)
                print(f"{len(phase.matchs)} matchs de groupes ont ete ajoutes a la competition.")


        elif choix == "15":
            print("15.Quitter")
            print("Merci et à bientôt")
            print()
            break


        else:
            print()
            print("Choix invalide. Essayez encore.")