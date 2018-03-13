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
    
    def jeu(self):
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
    maitre = {'sens': 1, 'x': 11, 'y': 5}  # Le personnage auquel l'épée est attachée valeur d'exemple
    global maitre
    jeu = {'position': [{'nom': 'j1', 'x': 13, 'y': 4}], # l'objet de la classe maitre, qui tient entre autres une liste de dictionnaires représentants les collisions.
          }
    global jeu

    #Méthodes
    def __init__(self, name):
        self.name = name
        return name

    def coup(self):
        if maitre.sens == 1 : #si le maître est tourné vers la droite
            case_frappe = {'nom': self.name, 'x': maitre.get('x') + 1, 'y': maitre.get('y')} #unobjet 'collisionable' est représenté par
            # un dico contenant {nom-de-lobjet, coordX, coordY}

        else :
            case_frappe = {'nom': self.name, 'x': maitre.get('x') - 1, 'y': maitre.get('y')} 
        
        for col in jeu.get('position') :
            if col.get('nom') == case_frappe.get('nom'):
                del jeu.get('position')[case_frappe.get('nom')]
        
        jeu.get('position').append(case_frappe.copy())
        return jeu







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

