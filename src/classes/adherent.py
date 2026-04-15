from src.classes.abonnement import Abonnement

class Adherent:
    """
    Représente un membre du club qui possède un abonnement.
    """
    def __init__(self, nom, solde, type_abo="ticket"):
        self.nom = nom
        self.solde = solde
        self.abonnement = Abonnement(type_abo)

    def souscrire_forfait(self):
        """Passe l'adhérent au forfait et déduit les 200€."""
        if self.abonnement.type_abo == "forfait":
            return # Déjà au forfait
            
        nouveau_abo = Abonnement("forfait")
        cout = nouveau_abo.get_cout_initial()
        
        # On utilise debit_solde pour déduire les frais (et lever l'erreur si besoin)
        self.debit_solde(cout)
        self.abonnement = nouveau_abo

    def get_prix_seance(self, type_sport):
        """Demande le prix à l'objet abonnement."""
        return self.abonnement.get_prix_sport(type_sport)

    def debit_solde(self, montant):
        """Vérifie le solde et déduit le montant."""
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant
