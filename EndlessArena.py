# -*- coding: utf-8 -*-

# Les imports


# Les variables globales


# Les classes
class Univers(object):
    """La classe générale, qui gère l'initialisation, les autres objets et les contrôleurs"""
    # Attributs
    
    # Méthodes
    def __init__(self):
        """ Initialisation """
        pass
    
    def affichage(self):
        pass
    
    def menus(self):
        pass
    
    def checkChutePersos(self):
        pass
    
    def checkMeurtrePersos(self):
        pass
    
    def compteurDePoints(self):
        pass

class Plateforme(object):
    """La classe qui gère les plateformes"""
    #Attributs
    positionX = 0 #La position en X
    positionY = 0 #La position en Y
    vitesse = 0 #La vitesse
    
    #Méthodes
    def deplacement(self):
        pass
    

class Personnage(object):
    """La classe qui gère les personnages"""
    #Attributs
    contrôleur = 0  # le contrôleur auquel il est relié


    #Méthodes

    def __init__(self, name):
        self.nom = name
        self.position_perso = {'nom': self.nom, 'x': 1, 'y': 0, 'sens': 1}


    def deplacementDroite(self):
        self.position_perso['sens'] = 1
        self.position_perso['x'] += 1

    def deplacementGauche(self):
        self.position_perso['sens'] = 1
        self.position_perso['x'] -= 1

    def saut(self):
        pass

    

class Epee(object):
    """La classe qui gère les personnages"""
    #Attributs
    maitre = {'sens': 1, 'x': 11, 'y': 5}  # Le personnage auquel l'épée est attachée valeur d'exemple

    jeu = {'collisions': [{'nom': 'j1', 'x': 13, 'y': 4}], # l'objet de la classe maitre, qui tient entre autres une liste de dictionnaires représentants les collisions.
           'case_touchées':[]} #les cases ou se touchent deux objets


    #Méthodes
    def __init__(self, name):
        self.nom = name
        self.position_epee = {'nom': self.nom, 'x': maitre.get('x'), 'y': maitre.get('y')}


    def coup(self):
        if maitre.sens == 1 : #si le maître est tourné vers la droite
            self.position_epee['x'] += 1

        else :
            self.position_epee['x'] += 1

class Grappin(object):
    """La classe qui gère les personnages"""
    #Attributs
    maitre =  0 #Le personnage auquel l'épée est attachée

    
    #Méthodes
    def lance(self):
        pass
    
    def tracte(self):
        pass
    
    def tranche(self):
        pass
# Le programme principal


#Univers(lesArguments)

