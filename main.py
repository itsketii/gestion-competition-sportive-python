from DB_app_console_CAN_Ketsia import intialiser_db, charger_competition
from menu import menu_demarage
from competition import Competition
from  mot_de_passe import mdp


print()
mdp()
print()
competition = Competition("CAN 2025", "Coupe d'Afrique des Nations 2025", "01-01-2025", "10-02-2025")
print(f"Bienvenu dans le gestionnaire de la {competition.nom} : {competition.description}")
print(f"Cette compétion se tient du {competition.date_debut} au {competition.date_fin}")
print()
intialiser_db()
charger_competition(competition)
menu_demarage(competition)

