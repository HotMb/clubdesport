import requests

class Reservation:
    """
    Gère la logique de réservation entre un adhérent et une salle.
    """
    def __init__(self, adherent, salle, horaire):
        self.adherent = adherent
        self.salle = salle
        self.horaire = horaire

    def confirmer(self):
        """
        Tente de confirmer la réservation.
        Vérifie la disponibilité de la salle et le solde de l'adhérent.
        """
        # 1. Calcul du prix selon le sport de la salle
        prix = self.adherent.get_prix_seance(self.salle.type_sport)
        
        # 2. Vérification du solde (debit_solde lèvera une erreur si insuffisant)
        self.adherent.debit_solde(prix)
        
        # 3. Ajout à la salle (ajouter_inscrit lèvera une erreur si salle complète)
        self.salle.ajouter_inscrit(self.adherent.nom)

    def recuperer_registre_distant(self, type_sport):
        """
        Interroge le site web pour récupérer la liste des réservations existantes.
        """
        url = f"http://notreclubdesport.fr/{type_sport}/reservations.txt"
        try:
            reponse = requests.get(url)
            # On sépare le texte par ligne pour obtenir une liste
            return reponse.text.strip().split('\n')
        except Exception as e:
            return []
