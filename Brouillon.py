import random

from poste import Poste
from joueur import Joueur
from equipe import Equipe
from match import Match
from competition import Competition



poste_1 = Poste("Gardien de But", "Arrête les tirs et protège le but")
poste_2 = Poste("Défenseur Centrale", "Bloque les attaquants dans l'axe")
poste_3 = Poste("Arrère Droit", "Défend et attaque sur le côté droit")
poste_4 = Poste("Arrière Gauche", "Défend et attaque sur le côté gauche")
poste_5 = Poste("Milieur Défensif", "Récupère les ballons")
poste_6 = Poste("Milieu Central", "Distribue le jeu")
poste_7 = Poste("Milieu Offensif", "Crée les occasions")
poste_8 = Poste("Ailier Droit", "Attaque par la droite")
poste_9 = Poste("Ailier Gauche", "Attaque par la gauche")
poste_10 = Poste("Avant-Centre", "Marque les buts")



joueur_1 = Joueur("Fofana", "Yahia", "Ivoirien", "1,94m", "88 Kg", "Droit", poste_1)
joueur_2 = Joueur("Lafont", "Alban", "Franco-Ivoirien", "1,96m", "82 Kg", "Droit", poste_1)
joueur_3 = Joueur("Kone", "Mohamed", "Ivoirien", "1,86m", "78 Kg", "Droit", poste_1)
joueur_4 = Joueur("Diomande", "Ousmane", "Ivoirien", "1,81m", "82 Kg", "", poste_2)
joueur_5 = Joueur("Ndicka", "Evan", "Franco-Ivoirien", "1,92m", "82 Kg", "Gauche", poste_2)
joueur_6 = Joueur("Kossounou", "Odilon", "Ivoirien", "1,91m", "97 Kg", "Gauche", poste_2 )
joueur_7 = Joueur("Agbadou", "Emmanuel", "Ivoirien", "1,92m", "96 Kg", "Droit", poste_2)
joueur_8 = Joueur("Gbamin", "Jean-Philippe", "Ivoirien", "1,86m", "83 Kg", "Droit", poste_2)
joueur_9 = Joueur("Boly", "Willy", "Ivoirien", "1,95m", "97 Kg", "Gauche", poste_2)
joueur_10 = Joueur("Operi", "Christopher", "Ivoirien", "1,83m", "83 Kg", "Gauche", poste_4)
joueur_11 = Joueur("Doué", "Désiré", "Ivoirien", "1,87m", "78 Kg", "Gauche", poste_3)
joueur_12 = Joueur("Zohouri", "Armel", "Ivoirien", "1,76m", "76 Kg", "Gauche", poste_3)
joueur_13 = Joueur("Sangare", "Ibrahim", "Ivoirien", "1,91m", "77 Kg", "Gauche", poste_5)
joueur_14 = Joueur("Seri", "Jean Michaël", "Ivoirien", "1,68m", "73 Kg", "Droit", poste_5)
joueur_15 = Joueur("Oulaï", "Chris Inao", "Ivoirien", "1,73m", "78 Kg", "Droit", poste_6)
joueur_16 = Joueur("Kessié", "Franck", "Ivoirien", "1,83m", "87 Kg", "Droit", poste_6)
joueur_17 = Joueur("Fofana", "Seko", "Ivoirien", "1,85m", "73 Kg", "Gauche", poste_6)
joueur_18 = Joueur("Diomande", "Yan", "Ivoirien", "1,80m", "80 Kg", "Gauche", poste_6)
joueur_19 = Joueur("Toure", "Bazoumana", "Ivoirien", "1,90m", "90 Kg", "Gauche", poste_9)
joueur_20 = Joueur("Zaha", "Wilfred", "Ivoirien", "1,88m", "75 Kg", "Droit", poste_9)
joueur_21 = Joueur("Guiagon", "Parfait", "Ivoirien", "1,70m", "80 Kg", "Droit", poste_9)
joueur_22 = Joueur("Diallo", "Amad", "Ivoirien", "1,73m", "72 Kg", "Droit", poste_8)
joueur_23 = Joueur("Guessand", "Evann", "Franco-Ivoirien", "1,88m", "76 Kg", "Droit", poste_8)
joueur_24 = Joueur("Diakite", "Oumar", "Ivoirien", "1,85m", "79 Kg", "Gauche", poste_10)
joueur_25 = Joueur("Krasso", "Jean-Philippe", "Ivoirien", "1,87m", "75 Kg", "Droit", poste_10)
joueur_26 = Joueur("Bayo", "Vakoun", "Ivoirien", "1,84m", "72 Kg", "Gauche", poste_10)


joueur_27 = Joueur("Bounou", "Yassine", "Marocain", "1,95m", "78 Kg", "Gauche", poste_1)
joueur_28 = Joueur("Al Harrar", "El Mehdi", "Marocain", "1,92m", "75 Kg", "Droit", poste_1)
joueur_29 = Joueur("El Kajoui", "Munir", "Marocain", "1,90m", "73 Kg", "Droit", poste_1)
joueur_30 = Joueur("Aguerd", "Nayef", "Marocain", "1,90m", "76 Kg", "Gauche", poste_2)
joueur_31 = Joueur("Boudlal", "Abdelhamid", "Marocain", "1,90m", "80 Kg", "Droit", poste_2)
joueur_32 = Joueur("Saïs", "Romain", "Marocain", "1,90m", "70 Kg", "Gauche", poste_2)
joueur_33 = Joueur("Massina", "Adam", "Marocain", "1,91m", "70 Kg", "Gauche", poste_2)
joueur_34 = Joueur("El Yamiq", "Jawad", "Marocain", "1,93m", "83 Kg", "Droit", poste_2)
joueur_35 = Joueur("Salah-Eddine", "Anass", "Marocain", "1,81m", "66 Kg", "Gauche", poste_4)
joueur_36 = Joueur("Belammari", "Youssef", "Marocain", "1,80m", "", "Droit", poste_4)
joueur_37 = Joueur("Hakimi", "Achraf", "Marocain", "1,81m", "73 Kg", "Droit", poste_3)
joueur_38 = Joueur("Mazraoui", "Noussair", "Marocain", "1,83m", "70 Kg", "Droit", poste_3)
joueur_39 = Joueur("Chibi", "Mohamed", "Marocain", "1,80m", "70 kg", "Gauche", poste_3)
joueur_40 = Joueur("Amrabat", "Sofyan", "Marocain", "1,85m", "80 kg", "Droit", poste_5)
joueur_41 = Joueur("Targhalline", "Oussama", "Marocain", "1,85m", "78 kg", "Droit", poste_5 )
joueur_42 = Joueur("El Aynaoui", "Neil", "Marocain", "1,70m", "70 kg", "Gauche", poste_6)
joueur_43 = Joueur("Ounahi", "Azzedine", "Marocain", "1,78m", "68 Kg", "Droit", poste_6)
joueur_44 = Joueur("Saibari", "Ismael", "Marocain", "1,85m", "78 Kg", "Droit", poste_6)
joueur_45 = Joueur("El Khannouss", "Bilal", "Marocain", "1,80m", "70 Kg", "Droit", poste_6)
joueur_46 = Joueur("Ben Seghir", "Eliesse", "Marocain", "1,77m", "70 kg", "Droit", poste_9)
joueur_47 = Joueur("Ezzalzouli", "Abde", "Marocain", "1,77m", "68 kg", "Droit", poste_9)
joueur_48 = Joueur("Rahimi", "Soufiane", "Marocain", "1,78m", "70 kg", "Droit", poste_9)
joueur_49 = Joueur("Diaz", "Brahim", "Marocain", "1,71m", "68 kg", "Droit", poste_8)
joueur_50 = Joueur("Talbi","Chemsdine", "Marocain", "1,80m", "72 kg", "Droit", poste_8)
joueur_51 = Joueur("Akhomach", "Ilias", "Marocain", "1,72m", "66 kg", "Gauche", poste_8)
joueur_52 = Joueur("En-Nesyri", "Youssef", "Marocain", "1,92m", "80 kg", "Droit", poste_10)
joueur_53 = Joueur("Igamane", "Hamza", "Marocain", "1,843m", "78 kg", "Droit", poste_10)
joueur_54 = Joueur("El Kaabi", "Ayoub", "Marocain", "1,82m", "75 kg", "Droit", poste_10)


joueur_55 = Joueur("Onana","André", "Camerounais", "1,90m", "92 kg", "Droit", poste_1)
joueur_56 = Joueur("Epassy","Devis", "Camerounais", "1,89m", "82 Kg", "", poste_1)
joueur_57 = Joueur("Omossola", "Simon", "Camerounais", "1,91m", "85 Kg", "", poste_1)
joueur_58 = Joueur("Castelletto", "Jean-Charles", "Camerounais", "1,86m", "79 Kg", "Droit", poste_2)
joueur_59 = Joueur("Wooh", "Christopher", "Camerounais", "1,91m", "92 Kg", "Droit",poste_2)
joueur_60 = Joueur("Boyomo", "Enzo", "Camerounais", "1,84m", "80 Kg", "Droit", poste_2)
joueur_61 = Joueur("Ngadeu", "Michel", "Camerounais", "1,90m", "90 Kg", "Droit", poste_2)
joueur_62 = Joueur("Tchatchoua", "Jackson", "Camerounais", "1,82m", "75 Kg", "Droit", poste_3)
joueur_63 = Joueur("Tchamadeu", "Junior", "Camerounais", "1,83m", "78 Kg", "Droit", poste_3)
joueur_64 = Joueur("Tolo", "Nouhou", "Camerounais", "1,78m", "79 Kg", "Gauche", poste_3)
joueur_65 = Joueur("Yongwa", "Darlin", "Camerounais", "1,77m", "73 Kg", "Gauche", poste_3)
joueur_66 = Joueur("Baleba", "Carlos", "Camerounais", "1,79m", "76 Kg", "Gauche", poste_5)
joueur_67 = Joueur("Anguissa", "André-Frank", "Camerounais", "1,84m", "78 Kg", "Droit", poste_6)
joueur_68 = Joueur("Hongla", "Martin", "Camerounais", "1,81m", "77 Kg", "Droit", poste_6)
joueur_69 = Joueur("Avom", "Arthur", "Camerounais", "1,75m", "70 Kg", "Droit", poste_6)
joueur_70 = Joueur("Mbeumo", "Bryan", "Camerounais", "1,76m", "75 Kg", "Gauche", poste_8)
joueur_71 = Joueur("Bassogog", "Christian", "Camerounais", "1,73m", "72 Kg", "Gauche", poste_8)
joueur_72 = Joueur("Ngamaleu", "Moumi", "Camerounais", "1,81m", "74 Kg", "Droit", poste_9)
joueur_73 = Joueur("Aboubakar", "Vincent", "Camerounais", "1,84m", "82 Kg", "Droit", poste_10)
joueur_74 = Joueur("Magri", "Frank", "Camerounais", "1,78m", "76 Kg", "Droit", poste_10)
joueur_75 = Joueur("Namaso", "Danny", "Camerounais", "1,82m", "79 Kg", "Droit", poste_10)
joueur_76 = Joueur("Etta Eyong", "Karl", "Camerounais", "1,85m", "81 Kg", "Droit", poste_10)


joueur_77 = Joueur("Mendy", "Edourard", "Senegalais", "1,94m", "94 Kg", "Droit", poste_1)
joueur_78 = Joueur("Diaw", "Mory", "Senegalais", "1,97m", "80 Kg", "Droit", poste_1)
joueur_79 = Joueur("Seny", "Dieng", "Senegalais", "1,93m", "82 Kg", "Droit", poste_1)
joueur_80 = Joueur("Koulibaly", "Kalidou", "Senegalais", "1,86m", "89 Kg", "Droit", poste_2)
joueur_81 = Joueur("Niakhaté", "Moussa", "Senegalais", "1,90m", "82 Kg", "Gauche", poste_2)
joueur_82 = Joueur("Seck", "Abdoulaye", "Senegalais", "1,92m", "94 Kg", "Droit", poste_2)
joueur_83 = Joueur("Diallo", "Abdou", "Senegalais", "1,87m", "80 Kg", "Gauche", poste_2)
joueur_84 = Joueur("Diatta", "Krepin", "Senegalais", "1,75m", "70 Kg", "Droit", poste_3)
joueur_85 = Joueur("Mendy", "Formose", "Senegalais", "1,91m", "83 Kg", "Droit", poste_3)
joueur_86 = Joueur("Jakobs", "Ismail", "Senegalais", "1,84m", "74 Kg", "Gauche", poste_4)
joueur_87 = Joueur("Ballo-Touré", "Fode", "Senegalais", "1,82m", "78 Kg", "Gauche", poste_4)
joueur_88 = Joueur("Gueye", "Idriss Gana", "Senegalais", "1,74m", "66 Kg", "Droit", poste_5)
joueur_89 = Joueur("Camara", "Lamine", "Senegalais", "1,73m", "68 Kg", "Droit", poste_5)
joueur_90 = Joueur("Sarr", "Pape Matar", "Senegalais", "1,85m", "70 Kg", "Gauche", poste_5)
joueur_91 = Joueur("Ciss", "Pathe", "Senegalais", "1,86m", "75 Kg", "Droit", poste_5)
joueur_92 = Joueur("Gueye", "Pape", "Senegalais", "1,89m", "79 Kg", "Gauche", poste_5)
joueur_93 = Joueur("Mane", "Sadio", "Senegalais", "1,74m", "69 Kg", "Droit", poste_6)
joueur_94 = Joueur("Sarr", "Ismaila", "Senegalais", "1,85m", "76 Kg", "Gauche", poste_8)
joueur_95 = Joueur("Ndiaye", "Iliman", "Senegalais", "1,80m", "72 Kg", "Droit",  poste_7)
joueur_96 = Joueur("Jackson", "Nicolas", "Senegalais", "1,87m", "78 Kg", "Droit", poste_10)
joueur_97 = Joueur("Diallo", "Habib", "Senegalais", "1,86m", "80 Kg", "Droit", poste_10)
joueur_98 = Joueur("Dieng", "Bamba", "Senegalais", "1,78m", "73 Kg", "Droit", poste_10)
joueur_99 = Joueur("Seck", "Amadou", "Senegalais", "1,83m", "77 Kg", "Droit", poste_10)


joueur_100 = Joueur
joueur_101 = Joueur
joueur_102 = Joueur
joueur_103 = Joueur
joueur_104 = Joueur
joueur_105 = Joueur



equipe_ci = Equipe("Equipe Ivoirienne", "Orange-Blanc-Vert : 🇨🇮", [])
joueurs_ci = [
    joueur_1, joueur_2, joueur_3, joueur_4, joueur_5,
    joueur_6, joueur_7, joueur_8, joueur_9, joueur_10,
    joueur_11, joueur_12, joueur_13, joueur_14, joueur_15,
    joueur_16, joueur_17, joueur_18, joueur_19, joueur_20,
    joueur_21, joueur_22, joueur_23, joueur_24, joueur_25,
    joueur_26
    ]
for joueur in joueurs_ci:
    equipe_ci.ajouter_joueur(joueur)


equipe_maroc = Equipe("Equipe Marocaine", "Rouge-Vert : 🇲🇦", [])
joueurs_maroc = [
    joueur_27, joueur_28, joueur_29, joueur_30, joueur_31,
    joueur_32, joueur_33, joueur_34, joueur_35, joueur_36,
    joueur_37, joueur_38, joueur_39, joueur_40, joueur_41,
    joueur_42, joueur_43, joueur_44, joueur_45, joueur_46,
    joueur_47, joueur_48, joueur_49, joueur_50, joueur_51,
    joueur_52, joueur_53, joueur_54
    ]
for joueur in joueurs_maroc:
    equipe_maroc.ajouter_joueur(joueur)


equipe_cameroune = Equipe("Equipe Camerounaise", "Vert-Rouge-Jaune : 🇨🇲", [])
joueurs_cameroune = [
    joueur_55, joueur_56, joueur_57, joueur_58, joueur_59,
    joueur_60, joueur_61, joueur_62, joueur_63, joueur_64,
    joueur_65, joueur_66, joueur_67, joueur_68, joueur_69,
    joueur_70, joueur_71, joueur_72, joueur_73, joueur_74,
    joueur_75, joueur_76
]
for joueur in joueurs_cameroune:
    equipe_cameroune.ajouter_joueur(joueur)


equipe_senegale = Equipe("Equipe Senegalaise", "Vert-Jaune-Rouge : 🇸🇳", [])
joueurs_senegale = [
    joueur_77, joueur_78, joueur_79, joueur_80, joueur_81,
    joueur_82, joueur_83, joueur_84, joueur_85, joueur_86,
    joueur_87, joueur_88, joueur_89, joueur_90, joueur_91,
    joueur_92, joueur_93, joueur_94, joueur_95, joueur_96,
    joueur_97, joueur_98, joueur_99
]
for joueur in joueurs_senegale:
    equipe_senegale.ajouter_joueur(joueur)


def creer_match_aleatoire(equipes, max_buts=5):
    equipe1, equipe2 = random.sample(equipes, 2)
    buts1 = random.randint(0, max_buts)
    buts2 = random.randint(0, max_buts)
    score = f"{buts1}-{buts2}"

    if buts1 > buts2:
        vainqueur = equipe1
    elif buts2 > buts1:
        vainqueur = equipe2
    else:
        vainqueur = None
    return Match(equipe1, equipe2, score, vainqueur)

competition = Competition("CAN 2025", "Coupe d'Afrique des Nations", "2025-01-01", "2025-02-01")
competition.ajouter_equipe(equipe_ci)
competition.ajouter_equipe(equipe_maroc)
competition.ajouter_equipe(equipe_cameroune)
competition.ajouter_equipe(equipe_senegale)



# Tirage aleatoire des equipes, des score et du vainqueur.
match_1 = creer_match_aleatoire(competition.equipes)
competition.ajouter_match(match_1)



#Test
print(competition.nom)
print()
print("Equipes participantes")
print(equipe_ci.nom, ":", len(equipe_ci.joueurs), "joueurs")
print(equipe_maroc.nom, ":", len(equipe_maroc.joueurs), "joueurs")
print(equipe_cameroune.nom, ":", len(equipe_cameroune.joueurs), "joueurs")
print(equipe_senegale.nom, ":", len(equipe_senegale.joueurs), "joueurs")
print()
print("Match :", match_1.equipe1.nom, "VS", match_1.equipe2.nom, "| Score : ", match_1.score)
if match_1.vainqueur is None:
    print("Vainqueur : Match nul")
else:
    print("Vainqueur :", match_1.vainqueur.nom)

print()




