class Adherent:
    """
    Représente un membre du club avec son solde et son type d'abonnement.
    Types d'abonnement : 'ticket' ou 'forfait'.
    """
    def __init__(self, nom, solde, type_abonnement):
        self.nom = nom
        self.solde = solde
        self.type_abonnement = type_abonnement
        
        # Tarifs par sport et type d'abonnement
        self.tarifs = {
            "ticket": {"tennis": 30, "badminton": 20, "squash": 15},
            "forfait": {"tennis": 11, "badminton": 10, "squash": 9}
        }

    def get_prix_seance(self, type_sport):
        """Retourne le prix d'une séance selon le sport et l'abonnement."""
        return self.tarifs[self.type_abonnement].get(type_sport.lower(), 0)

    def debit_solde(self, montant):
        """Déduit un montant du solde si suffisant, sinon lève une erreur."""
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
