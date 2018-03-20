# -*- coding: utf-8 -*-

# Les imports


# Les variables globales


# Les classes
class Univers:
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
        joueurs = [joueur1; joueur2]
        for test in joueurs :
            if test.position_perso['y'] > tailleFenetreY:
                Univers.compteurDePoints(joueurs.index(test), -1)
                test.position_perso['y'] = positionInitialeY
                test.position_perso['x'] = positionInitialeX
    
    def checkMeurtrePersos(self):
        pass
    
    def compteurDePoints(self, joueur, increment):
        pass

class Plateforme:
    """La classe qui gère les plateformes"""
    
    #Méthodes
    def __init__(self, name, posX, posY):
        self.nom = name
        self.position_perso = {'x': posX, 'y': posY}
    
    def deplacement(self, deplacement):
        """Pour déplacer les plateformes, deplacement en pixel. deplacement > 0 ==> vers la droite ; deplacement < 0 ==> vers la gauche"""
        self.position_perso['y'] += deplacement
    

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

class Grappin:
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

