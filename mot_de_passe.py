import getpass
import sys


def _lire_mot_de_passe():
    if sys.stdin and sys.stdin.isatty():
        try:
            return getpass.getpass("Mot de passe: ")
        except Exception:
            pass

    print("Mot de passe visible dans cette console.")
    return input("Mot de passe: ")

def mdp():
    while True:
        print()
        print("Salut")
        print("Veuillez vous identifer")
        user_name = input("Nom de l'utilisateur: ")
        password = _lire_mot_de_passe()

        if user_name.strip() == "" or password.strip() == "":
            print("Veuillez renseigner le nom d'utilisateur et le mot de passe.")
        elif user_name != "Ketsia" or password != "IIT-350":
            print("Le nom d'utilisateur ou le mot de passe est incorrect.")
        else:
            print()
            print("Content de vous revoir.")
            break