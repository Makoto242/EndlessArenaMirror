# -*- coding: utf-8 -*-

# Les imports


# Les variables globales


# Les classes
class Univers:
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

class Plateforme:
    """La classe qui gère les plateformes"""
    #Attributs
    positionX = 0 #La position en X
    positionY = 0 #La position en Y
    vitesse = 0 #La vitesse
    
    #Méthodes
    def deplacement(self):
        pass
    

class Personnage:
    """La classe qui gère les personnages"""
    #Attributs
    contrôleur = 0 #le contrôleur auquel il est relié
    positionX = 0 #La position en X
    positionY = 0 #La position en Y
    
    #Méthodes
    def deplacement(self):
        pass
    
    def saut(self):
        pass
    
    def mort(self):
        pass
    

class Epee:
    """La classe qui gère les personnages"""
    #Attributs
    maitre =  0 #Le personnage auquel l'épée est attachée
    
    #Méthodes
    def coup(self):
        pass
    
    def donneCaseFrappee(self):
        pass

class Epee:
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

