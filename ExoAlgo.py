

#Création des classes

class Livre:
    def __init__(self, titre, auteur, isbn):
        self.titre = titre
        self.auteur = auteur
        self.isbn = isbn

class Magazine:
    def __init__(self, titre, numero, date_publication):
        self.titre = titre
        self.numero = numero
        self.date_publication = date_publication

class Utilisateur:
    def __init__(self, nom_utilisateur):
        self.nom_utilisateur = nom_utilisateur
        self.livres_empruntes = []

class Bibliothèque:
    def __init__(self):
        self.livres = []
        self.magazines = []
        self.utilisateurs = []

    def ajouter_livre(self, livre):
        self.livres.append(livre)

    def ajouter_magazine(self, magazine):
        self.magazines.append(magazine)

    def ajouter_utilisateur(self, utilisateur):
        self.utilisateurs.append(utilisateur)

    def emprunter_livre(self, utilisateur, livre):
        if livre in self.livres and livre not in utilisateur.livres_empruntes:
            utilisateur.livres_empruntes.append(livre)
            return True
        else:
            return False

    def rendre_livre(self, utilisateur, livre):
        if livre in utilisateur.livres_empruntes:
            utilisateur.livres_empruntes.remove(livre)
            return True
        else:
            return False

    def chercher_livre_par_titre(self, titre):
        livres_trouves = [livre for livre in self.livres if livre.titre == titre]
        return livres_trouves

    def chercher_livre_par_auteur(self, auteur):
        livres_trouves = [livre for livre in self.livres if livre.auteur == auteur]
        return livres_trouves

    def livres_empruntes_par_utilisateur(self, utilisateur):
        return utilisateur.livres_empruntes

# Fonction pour afficher le menu principal
def afficher_menu():
    print("\n=== Menu ===")
    print("1. Ajouter un livre")
    print("2. Emprunter un livre")
    print("3. Rendre un livre")
    print("4. Rechercher un livre par titre")
    print("5. Rechercher un livre par auteur")
    print("6. Afficher les livres empruntés par un utilisateur")
    print("7. Quitter")

if __name__ == "__main__":
    bibliotheque = Bibliothèque()

    while True:
        afficher_menu()
        choix = input("Choisissez une option (1-7) : ")

        if choix == "1":
            # Ajout d'un nouveau livre à la bibliothèque
            titre = input("Titre du livre : ")
            auteur = input("Auteur du livre : ")
            isbn = input("ISBN du livre : ")
            livre = Livre(titre, auteur, isbn)
            bibliotheque.ajouter_livre(livre)
            print("Livre ajouté avec succès à la bibliothèque.")

        elif choix == "2":
            # Emprunt d'un livre par un utilisateur
            nom_utilisateur = input("Nom de l'utilisateur : ")
            utilisateur = Utilisateur(nom_utilisateur)
            bibliotheque.ajouter_utilisateur(utilisateur)

            titre = input("Titre du livre à emprunter : ")
            livres_trouves = bibliotheque.chercher_livre_par_titre(titre)

            if len(livres_trouves) == 0:
                print("Aucun livre trouvé avec ce titre.")
            else:
                livre_a_emprunter = livres_trouves[0]  # Nous supposons qu'il n'y a qu'un seul livre avec ce titre
                if bibliotheque.emprunter_livre(utilisateur, livre_a_emprunter):
                    print(f"{livre_a_emprunter.titre} emprunté par {utilisateur.nom_utilisateur}.")
                else:
                    print(f"{livre_a_emprunter.titre} n'est pas disponible à l'emprunt.")

        elif choix == "3":
            # Rendre un livre emprunté par un utilisateur
            nom_utilisateur = input("Nom de l'utilisateur : ")
            utilisateur = Utilisateur(nom_utilisateur)

            titre = input("Titre du livre à rendre : ")
            livres_trouves = bibliotheque.chercher_livre_par_titre(titre)

            if len(livres_trouves) == 0:
                print("Aucun livre trouvé avec ce titre.")
            else:
                livre_a_rendre = livres_trouves[0]  # Nous supposons qu'il n'y a qu'un seul livre avec ce titre
                if bibliotheque.rendre_livre(utilisateur, livre_a_rendre):
                    print(f"{livre_a_rendre.titre} rendu avec succès par {utilisateur.nom_utilisateur}.")
                else:
                    print(f"{livre_a_rendre.titre} n'a pas été emprunté par {utilisateur.nom_utilisateur}.")

        elif choix == "4":
            # Recherche d'un livre par son titre
            titre = input("Titre du livre à rechercher : ")
            livres_trouves = bibliotheque.chercher_livre_par_titre(titre)

            if len(livres_trouves) == 0:
                print("Aucun livre trouvé avec ce titre.")
            else:
                print("Livres trouvés :")
                for livre in livres_trouves:
                    print(f"{livre.titre} - Auteur : {livre.auteur} - ISBN : {livre.isbn}")

        elif choix == "5":
            # Recherche d'un livre par son auteur
            auteur = input("Auteur du livre à rechercher : ")
            livres_trouves = bibliotheque.chercher_livre_par_auteur(auteur)

            if len(livres_trouves) == 0:
                print("Aucun livre trouvé avec cet auteur.")
            else:
                print("Livres trouvés :")
                for livre in livres_trouves:
                    print(f"{livre.titre} - Auteur : {livre.auteur} - ISBN : {livre.isbn}")

        elif choix == "6":
            # Afficher les livres empruntés par un utilisateur
            nom_utilisateur = input("Nom de l'utilisateur : ")
            utilisateur = Utilisateur(nom_utilisateur)
            livres_empruntes_utilisateur = bibliotheque.livres_empruntes_par_utilisateur(utilisateur)

            if len(livres_empruntes_utilisateur) == 0:
                print(f"Aucun livre emprunté par {utilisateur.nom_utilisateur}.")
            else:
                print(f"Livres empruntés par {utilisateur.nom_utilisateur}:")
                for livre in livres_empruntes_utilisateur:
                    print(f"{livre.titre} - Auteur : {livre.auteur} - ISBN : {livre.isbn}")

        elif choix == "7":
            # Quitter
            print("Merci d'avoir utilisé notre logiciel de gestion de bibliothèque. Au revoir !")
            break

        else:
            print("Option invalide. Veuillez saisir un nombre entre 1 et 7.")


