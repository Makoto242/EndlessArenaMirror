# -*- coding: utf-8 -*-

# Les imports


# Les variables globales


# Les classes
class Univers(object):
    """La classe générale, qui gère l'initialisation, les autres objets et les contrôleurs"""
    # Attributs
    jeu = [] #la seule variable qui va voyager, contient la position de chaque objet sous la forme {nom, x, y}
    
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

    def jeu(self):
        pass

class Personnage(object):
    """La classe qui gère les personnages"""
    #Méthodes

    def __init__(self, name):
        self.nom = name
        self.position_perso = {'nom': self.nom, 'x': 1, 'y': 0, 'sens': 1}


    def deplacementDroite(self):
        self.position_perso['sens'] = 1
        self.position_perso['x'] += 1

    def deplacementGauche(self):
        self.position_perso['sens'] = 0
        self.position_perso['x'] -= 1

    def saut(self):
        self.position_perso['y'] += 5 ##trés mauvais, à améliorer

    

class Epee(object):
    """La classe qui gère les épées"""
    #Attributs

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
    """La classe qui gère les grappins"""

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

