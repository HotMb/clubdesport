class Salle:
    """
    Gère une salle de sport, sa capacité et ses inscrits.
    """
    def __init__(self, nom, type_sport, capacite):
        self.nom = nom
        self.type_sport = type_sport
        self.capacite = capacite
        self.inscrits = []

    def est_disponible(self):
        """Retourne vrai s'il reste de la place dans la salle."""
        return self.capacite > 0

    def ajouter_inscrit(self, nom_inscrit):
        """
        Ajoute une personne à la liste des inscrits et réduit la capacité.
        Lève une erreur si la salle est déjà pleine.
        """
        if not self.est_disponible():
            raise ValueError("Salle complète")
        
        self.inscrits.append(nom_inscrit)
        self.capacite -= 1