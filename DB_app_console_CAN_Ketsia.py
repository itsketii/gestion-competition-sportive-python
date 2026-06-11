import sqlite3
from poste import Poste
from equipe import Equipe
from joueur import Joueur
from match import Match

def etabliblir_connection():
    connection = sqlite3.connect('app_console_CAN_Ketsia.db')
    return connection


def intialiser_db():
    connection = etabliblir_connection()
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    cursor.execute('''CREATE TABLE IF NOT EXISTS postes(
                                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           nom TEXT NOT NULL,
                                                           description TEXT)
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS equipes(
                                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            nom TEXT NOT NULL,
                                                            drapeau TEXT)
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS joueurs(
                                                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                            nom TEXT NOT NULL,
                                                            prenoms TEXT NOT NULL,
                                                            nationalite TEXT,
                                                            taille TEXT,
                                                            poids TEXT,
                                                            pied_fort TEXT,
                                                            poste_id INTEGER,
                                                            equipe_id INTEGER,
                                                            FOREIGN KEY (poste_id) REFERENCES postes(id),
        FOREIGN KEY (equipe_id) REFERENCES equipes(id))
                   ''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS matchs(
                                                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           date TEXT,
                                                           equipe_1_id INTEGER,
                                                           equipe_2_id INTEGER,
                                                           score TEXT,
                                                           vainqueur_id INTEGER,
                                                           FOREIGN KEY (equipe_1_id) REFERENCES equipes(id),
        FOREIGN KEY (equipe_2_id) REFERENCES equipes(id),
        FOREIGN KEY (vainqueur_id) REFERENCES equipes(id))
                   ''')

    connection.commit()
    connection.close()


def sauvegarder_competition(competition):
    connection = etabliblir_connection()
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    # On remplace la sauvegarde precedente pour garder une base coherente.
    cursor.execute("DELETE FROM matchs")
    cursor.execute("DELETE FROM joueurs")
    cursor.execute("DELETE FROM equipes")
    cursor.execute("DELETE FROM postes")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name IN ('matchs', 'joueurs', 'equipes', 'postes')")

    for poste in competition.postes:
        cursor.execute('''INSERT INTO postes(nom, description) VALUES (?, ?)''',
                       (poste.nom, poste.description))
        poste.id = cursor.lastrowid

    for equipe in competition.equipes:
        cursor.execute('''INSERT INTO equipes(nom, drapeau) VALUES (?, ?)''',
                       (equipe.nom, equipe.drapeau))
        equipe.id = cursor.lastrowid

    for joueur in competition.joueurs:
        poste_id = joueur.poste.id if getattr(joueur, "poste", None) else None
        equipe_id = joueur.equipe.id if getattr(joueur, "equipe", None) else None
        cursor.execute('''INSERT INTO joueurs(nom, prenoms, nationalite, taille, poids, pied_fort, poste_id, equipe_id) VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                       (joueur.nom, joueur.prenoms, joueur.nationalite, joueur.taille, joueur.poids, joueur.pied_fort, poste_id, equipe_id))

    for match in competition.matchs:
        equipe_1_id = match.equipe1.id if getattr(match, "equipe1", None) else None
        equipe_2_id = match.equipe2.id if getattr(match, "equipe2", None) else None
        vainqueur_id = match.vainqueur.id if getattr(match, "vainqueur", None) else None
        cursor.execute('''INSERT INTO matchs(date, equipe_1_id, equipe_2_id, score, vainqueur_id) VALUES (?, ?, ?, ?, ?)''',
                       (match.date, equipe_1_id, equipe_2_id, match.score, vainqueur_id))

    connection.commit()
    connection.close()
    print("Données sauvegardées !")


def charger_competition(competition):
    connection = etabliblir_connection()
    cursor = connection.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    competition.postes.clear()
    competition.equipes.clear()
    competition.joueurs.clear()
    competition.matchs.clear()

    postes_par_id = {}
    equipes_par_id = {}

    cursor.execute("SELECT id, nom, description FROM postes")
    for poste_id, nom, description in cursor.fetchall():
        poste = Poste(nom, description)
        poste.id = poste_id
        competition.postes.append(poste)
        postes_par_id[poste_id] = poste

    cursor.execute("SELECT id, nom, drapeau FROM equipes")
    for equipe_id, nom, drapeau in cursor.fetchall():
        equipe = Equipe(nom, drapeau, [])
        equipe.id = equipe_id
        competition.equipes.append(equipe)
        equipes_par_id[equipe_id] = equipe

    cursor.execute("SELECT id, nom, prenoms, nationalite, taille, poids, pied_fort, poste_id, equipe_id FROM joueurs")
    for joueur_id, nom, prenoms, nationalite, taille, poids, pied_fort, poste_id, equipe_id in cursor.fetchall():
        poste = postes_par_id.get(poste_id)
        equipe = equipes_par_id.get(equipe_id)
        joueur = Joueur(nom, prenoms, nationalite, taille, poids, pied_fort, poste, equipe)
        joueur.id = joueur_id
        competition.joueurs.append(joueur)
        if equipe is not None:
            equipe.ajouter_joueur(joueur)

    cursor.execute("SELECT id, date, equipe_1_id, equipe_2_id, score, vainqueur_id FROM matchs")
    for match_id, date, equipe_1_id, equipe_2_id, score, vainqueur_id in cursor.fetchall():
        equipe1 = equipes_par_id.get(equipe_1_id)
        equipe2 = equipes_par_id.get(equipe_2_id)
        vainqueur = equipes_par_id.get(vainqueur_id)
        if equipe1 is not None and equipe2 is not None:
            match = Match(date, equipe1, equipe2, score, vainqueur)
            match.id = match_id
            competition.matchs.append(match)

    connection.close()
