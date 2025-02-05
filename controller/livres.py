class Livres:
    
    def __init__(self, titre_livre, auteur_livre, code_isbn_livre, nb_pages_livre, genre_livre, type_livre, annee_livre, etat_livre):
        self.titre_livre = titre_livre
        self.auteur_livre = auteur_livre
        self.code_isbn_livre = code_isbn_livre
        self.nb_pages_livre = nb_pages_livre
        self.genre_livre = genre_livre
        self.type_livre = type_livre
        self.annee_livre = annee_livre
        self.etat_livre = etat_livre
        
    def emprunter_livre(self):
        pass
    
    def retourner_livre(self):
        pass
    
    def rechercher_livre(self):
        pass
    
    class Livre_papier(Livres):
        pass
    
    class livre_numerique(Livres):
        pass